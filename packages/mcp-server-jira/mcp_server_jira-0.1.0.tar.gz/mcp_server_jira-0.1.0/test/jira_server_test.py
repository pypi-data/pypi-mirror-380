import pytest
import json
from unittest.mock import AsyncMock, patch
import httpx

from mcp_server_jira.server import (
    JiraServer, 
    JiraError, 
    validate_jira_token, 
    validate_issue_key, 
    validate_jira_url,
    JiraIssue,
    JiraTransition,
    TransitionsResult,
    WorklogResult,
    SearchResult
)


class TestValidationFunctions:
    """Test validation utility functions"""
    
    @pytest.mark.parametrize(
        "token,expected_error",
        [
            ("", "Invalid token: Token must have at least 10 characters"),
            ("   ", "Invalid token: Token must have at least 10 characters"),
            ("short", "Invalid token: Token must have at least 10 characters"),
            ("valid_token_123", None),  # Valid case
            ("  valid_token_123  ", None),  # Valid with whitespace
        ]
    )
    def test_validate_jira_token(self, token, expected_error):
        if expected_error:
            with pytest.raises(JiraError, match=expected_error):
                validate_jira_token(token)
        else:
            result = validate_jira_token(token)
            assert result == token.strip()

    @pytest.mark.parametrize(
        "issue_key,expected_result,expected_error",
        [
            ("LTC-4261", "LTC-4261", None),
            ("ltc-4261", "LTC-4261", None),  # Should be uppercase
            ("  PROJ-123  ", "PROJ-123", None),  # Should strip whitespace
            ("", None, "Invalid issue key format"),
            ("INVALID", None, "Invalid issue key format"),
            ("NO-DASH", None, "Invalid issue key format"),
        ]
    )
    def test_validate_issue_key(self, issue_key, expected_result, expected_error):
        if expected_error:
            with pytest.raises(JiraError, match=expected_error):
                validate_issue_key(issue_key)
        else:
            result = validate_issue_key(issue_key)
            assert result == expected_result

    @pytest.mark.parametrize(
        "base_url,expected",
        [
            ("", "https://jira.telefonica.com.br"),
            ("https://jira.company.com", "https://jira.company.com"),
            ("http://jira.company.com/", "http://jira.company.com"),
            ("jira.company.com", "https://jira.company.com"),
            ("jira.company.com/", "https://jira.company.com"),
        ]
    )
    def test_validate_jira_url(self, base_url, expected):
        result = validate_jira_url(base_url)
        assert result == expected


class TestJiraServer:
    """Test JiraServer business logic"""

    @pytest.fixture
    def jira_server(self):
        return JiraServer("https://test-jira.com")

    @pytest.fixture
    def valid_token(self):
        return "valid_bearer_token_123"

    @pytest.fixture
    def mock_issue_response(self):
        return {
            "key": "TEST-123",
            "fields": {
                "summary": "Test Issue",
                "status": {"name": "In Progress"},
                "assignee": {"displayName": "John Doe"},
                "reporter": {"displayName": "Jane Smith"},
                "created": "2024-01-01T10:00:00.000+0000",
                "updated": "2024-01-02T12:00:00.000+0000",
                "description": "Test description",
                "issuetype": {"name": "Bug"},
                "priority": {"name": "High"}
            }
        }

    @pytest.mark.asyncio
    async def test_get_issue_success(self, jira_server, valid_token, mock_issue_response):
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_issue_response
            
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            result = await jira_server.get_issue(valid_token, "TEST-123")
            
            assert isinstance(result, JiraIssue)
            assert result.key == "TEST-123"
            assert result.summary == "Test Issue"
            assert result.status == "In Progress"
            assert result.assignee == "John Doe"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "status_code,expected_error",
        [
            (401, "Authentication failed. Please check your token."),
            (404, "Issue TEST-123 not found."),
            (500, "Jira API error: 500"),
        ]
    )
    async def test_get_issue_errors(self, jira_server, valid_token, status_code, expected_error):
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = status_code
            mock_response.text = "Server Error"
            
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            with pytest.raises(JiraError, match=expected_error):
                await jira_server.get_issue(valid_token, "TEST-123")

    @pytest.mark.asyncio
    async def test_get_transitions_success(self, jira_server, valid_token, mock_issue_response):
        transitions_response = {
            "transitions": [
                {
                    "id": "11",
                    "name": "To Do",
                    "to": {"name": "To Do"}
                },
                {
                    "id": "21", 
                    "name": "Done",
                    "to": {"name": "Done"}
                }
            ]
        }
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 200
            mock_response.json.return_value = transitions_response
            
            # Mock get_issue call for current status
            mock_issue_response_obj = AsyncMock()
            mock_issue_response_obj.status_code = 200
            mock_issue_response_obj.json.return_value = mock_issue_response
            
            mock_client.return_value.__aenter__.return_value.get.side_effect = [
                mock_response,  # transitions call
                mock_issue_response_obj  # get_issue call
            ]
            
            result = await jira_server.get_transitions(valid_token, "TEST-123")
            
            assert isinstance(result, TransitionsResult)
            assert result.issue_key == "TEST-123"
            assert result.current_status == "In Progress"
            assert len(result.available_transitions) == 2
            assert result.available_transitions[0].name == "To Do"

    @pytest.mark.asyncio
    async def test_transition_issue_success(self, jira_server, valid_token, mock_issue_response):
        with patch('httpx.AsyncClient') as mock_client:
            # Mock transition POST response
            mock_transition_response = AsyncMock()
            mock_transition_response.status_code = 204
            
            # Mock get_issue response for updated issue
            mock_get_response = AsyncMock()
            mock_get_response.status_code = 200
            mock_get_response.json.return_value = mock_issue_response
            
            mock_client.return_value.__aenter__.return_value.post.return_value = mock_transition_response
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_get_response
            
            result = await jira_server.transition_issue(valid_token, "TEST-123", "11")
            
            assert isinstance(result, JiraIssue)
            assert result.key == "TEST-123"

    @pytest.mark.asyncio
    async def test_add_worklog_success(self, jira_server, valid_token):
        worklog_response = {
            "timeSpent": "1h",
            "comment": "Work completed",
            "author": {"displayName": "John Doe"},
            "created": "2024-01-02T14:00:00.000+0000"
        }
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 201
            mock_response.json.return_value = worklog_response
            
            mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
            
            result = await jira_server.add_worklog(valid_token, "TEST-123", "1h", "Work completed")
            
            assert isinstance(result, WorklogResult)
            assert result.issue_key == "TEST-123"
            assert result.time_spent == "1h"
            assert result.comment == "Work completed"
            assert result.author == "John Doe"

    @pytest.mark.asyncio
    async def test_search_issues_success(self, jira_server, valid_token):
        search_response = {
            "total": 1,
            "issues": [
                {
                    "key": "TEST-123",
                    "fields": {
                        "summary": "Test Issue",
                        "status": {"name": "In Progress"},
                        "assignee": {"displayName": "John Doe"},
                        "reporter": {"displayName": "Jane Smith"},
                        "created": "2024-01-01T10:00:00.000+0000",
                        "updated": "2024-01-02T12:00:00.000+0000",
                        "description": "Test description",
                        "issuetype": {"name": "Bug"},
                        "priority": {"name": "High"}
                    }
                }
            ]
        }
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 200
            mock_response.json.return_value = search_response
            
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            result = await jira_server.search_issues(valid_token, "assignee = currentUser()")
            
            assert isinstance(result, SearchResult)
            assert result.total == 1
            assert result.jql == "assignee = currentUser()"
            assert len(result.issues) == 1
            assert result.issues[0].key == "TEST-123"

    @pytest.mark.asyncio
    async def test_network_error_handling(self, jira_server, valid_token):
        with patch('httpx.AsyncClient') as mock_client:
            mock_client.return_value.__aenter__.return_value.get.side_effect = httpx.RequestError("Network error")
            
            with pytest.raises(JiraError, match="Network error connecting to Jira"):
                await jira_server.get_issue(valid_token, "TEST-123")

    def test_headers_generation(self, jira_server):
        token = "test_token_123"
        headers = jira_server._get_headers(token)
        
        expected_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json', 
            'Authorization': 'Bearer test_token_123'
        }
        
        assert headers == expected_headers


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "issue_key_input,expected_normalized",
        [
            ("ltc-4261", "LTC-4261"),
            ("  PROJ-123  ", "PROJ-123"),
            ("abc-999", "ABC-999"),
        ]
    )
    async def test_issue_key_normalization(self, issue_key_input, expected_normalized):
        jira_server = JiraServer()
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "key": expected_normalized,
                "fields": {
                    "summary": "Test",
                    "status": {"name": "Open"},
                    "assignee": None,
                    "reporter": {"displayName": "Test User"},
                    "created": "2024-01-01T00:00:00.000+0000",
                    "updated": "2024-01-01T00:00:00.000+0000",
                    "description": "",
                    "issuetype": {"name": "Task"},
                    "priority": {"name": "Medium"}
                }
            }
            
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            result = await jira_server.get_issue("valid_token_123", issue_key_input)
            assert result.key == expected_normalized

    @pytest.mark.parametrize(
        "jql_query,expected_jql",
        [
            ("assignee = currentUser()", "assignee = currentUser()"),
            ("project = TEST AND status = 'In Progress'", "project = TEST AND status = 'In Progress'"),
            ("created >= -7d", "created >= -7d"),
        ]
    )
    @pytest.mark.asyncio
    async def test_jql_queries(self, jql_query, expected_jql):
        jira_server = JiraServer()
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "total": 0,
                "issues": []
            }
            
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            result = await jira_server.search_issues("valid_token_123", jql_query)
            assert result.jql == expected_jql


if __name__ == "__main__":
    pytest.main([__file__])