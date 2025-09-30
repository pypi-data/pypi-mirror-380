from datetime import datetime
from enum import Enum
import json
from typing import Sequence, Optional
import httpx
from urllib.parse import urlparse

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from mcp.shared.exceptions import McpError

from pydantic import BaseModel, Field, validator


class JiraTools(str, Enum):
    GET_ISSUE = "get_issue"
    GET_TRANSITIONS = "get_transitions"
    TRANSITION_ISSUE = "transition_issue"
    ADD_WORKLOG = "add_worklog"
    SEARCH_ISSUES = "search_issues"


class JiraIssue(BaseModel):
    key: str
    summary: str
    status: str
    assignee: Optional[str] = None
    reporter: str
    created: str
    updated: str
    description: Optional[str] = None
    issue_type: str
    priority: str


class JiraTransition(BaseModel):
    id: str
    name: str
    to_status: str


class TransitionsResult(BaseModel):
    issue_key: str
    current_status: str
    available_transitions: list[JiraTransition]


class WorklogResult(BaseModel):
    issue_key: str
    time_spent: str
    comment: str
    author: str
    created: str


class SearchResult(BaseModel):
    total: int
    issues: list[JiraIssue]
    jql: str


class JiraError(Exception):
    """Custom exception for Jira operations"""
    pass


def validate_jira_token(token: str) -> str:
    """Validate Jira token format"""
    if not token or len(token.strip()) < 10:
        raise JiraError("Invalid token: Token must have at least 10 characters")
    return token.strip()


def validate_issue_key(issue_key: str) -> str:
    """Validate Jira issue key format"""
    issue_key = issue_key.strip().upper()
    if not issue_key or '-' not in issue_key:
        raise JiraError(f"Invalid issue key format: {issue_key}. Expected format: PROJECT-123")
    return issue_key


def validate_jira_url(base_url: str) -> str:
    """Validate and normalize Jira base URL"""
    if not base_url:
        return "https://jira.telefonica.com.br"
    
    parsed = urlparse(base_url)
    if not parsed.scheme:
        base_url = f"https://{base_url}"
    
    return base_url.rstrip('/')


class JiraServer:
    def __init__(self, base_url: str = "https://jira.telefonica.com.br", default_token: str | None = None):
        self.base_url = validate_jira_url(base_url)
        self.default_token = default_token
    
    def _get_headers(self, token: str | None = None) -> dict:
        """Get HTTP headers for Jira API requests"""
        # Use provided token, or fall back to default token
        auth_token = token or self.default_token
        if not auth_token:
            raise JiraError("No authentication token provided. Either pass token parameter or configure default token.")
        
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {validate_jira_token(auth_token)}'
        }
    
    async def get_issue(self, token: str | None, issue_key: str) -> JiraIssue:
        """Get detailed information about a Jira issue"""
        issue_key = validate_issue_key(issue_key)
        url = f"{self.base_url}/rest/api/2/issue/{issue_key}"
        
        async with httpx.AsyncClient(verify=False, timeout=30.0) as client:
            try:
                response = await client.get(url, headers=self._get_headers(token))
                
                if response.status_code == 401:
                    raise JiraError("Authentication failed. Please check your token.")
                elif response.status_code == 404:
                    raise JiraError(f"Issue {issue_key} not found.")
                elif response.status_code != 200:
                    raise JiraError(f"Jira API error: {response.status_code} - {response.text}")
                
                data = response.json()
                fields = data['fields']
                
                return JiraIssue(
                    key=data['key'],
                    summary=fields['summary'],
                    status=fields['status']['name'],
                    assignee=fields['assignee']['displayName'] if fields['assignee'] else None,
                    reporter=fields['reporter']['displayName'],
                    created=fields['created'],
                    updated=fields['updated'],
                    description=fields.get('description', ''),
                    issue_type=fields['issuetype']['name'],
                    priority=fields['priority']['name']
                )
                
            except httpx.TimeoutException:
                raise JiraError(f"Timeout connecting to Jira at {self.base_url}")
            except httpx.ConnectError:
                raise JiraError(f"Cannot connect to Jira at {self.base_url}. Check URL and network connectivity.")
            except httpx.RequestError as e:
                raise JiraError(f"Network error connecting to Jira: {str(e)}")
    
    async def get_transitions(self, token: str | None, issue_key: str) -> TransitionsResult:
        """Get available transitions for a Jira issue"""
        issue_key = validate_issue_key(issue_key)
        url = f"{self.base_url}/rest/api/2/issue/{issue_key}/transitions"
        
        async with httpx.AsyncClient(verify=False, timeout=30.0) as client:
            try:
                response = await client.get(url, headers=self._get_headers(token))
                
                if response.status_code == 401:
                    raise JiraError("Authentication failed. Please check your token.")
                elif response.status_code == 404:
                    raise JiraError(f"Issue {issue_key} not found.")
                elif response.status_code != 200:
                    raise JiraError(f"Failed to get transitions: {response.status_code} - {response.text}")
                
                data = response.json()
                
                transitions = []
                for trans in data['transitions']:
                    transitions.append(JiraTransition(
                        id=trans['id'],
                        name=trans['name'],
                        to_status=trans['to']['name']
                    ))
                
                # Get current status
                issue = await self.get_issue(token, issue_key)
                
                return TransitionsResult(
                    issue_key=issue_key,
                    current_status=issue.status,
                    available_transitions=transitions
                )
                
            except httpx.TimeoutException:
                raise JiraError(f"Timeout connecting to Jira at {self.base_url}")
            except httpx.ConnectError:
                raise JiraError(f"Cannot connect to Jira at {self.base_url}. Check URL and network connectivity.")
            except httpx.RequestError as e:
                raise JiraError(f"Network error: {str(e)}")
    
    async def transition_issue(self, token: str | None, issue_key: str, transition_id: str) -> JiraIssue:
        """Execute a transition on a Jira issue"""
        issue_key = validate_issue_key(issue_key)
        url = f"{self.base_url}/rest/api/2/issue/{issue_key}/transitions"
        
        payload = {
            "transition": {
                "id": transition_id
            }
        }
        
        async with httpx.AsyncClient(verify=False) as client:
            try:
                response = await client.post(
                    url, 
                    json=payload, 
                    headers=self._get_headers(token)
                )
                
                if response.status_code not in [200, 204]:
                    raise JiraError(f"Transition failed: {response.status_code} - {response.text}")
                
                # Return updated issue
                return await self.get_issue(token, issue_key)
                
            except httpx.RequestError as e:
                raise JiraError(f"Network error: {str(e)}")
    
    async def add_worklog(self, token: str | None, issue_key: str, time_spent: str, comment: str = "") -> WorklogResult:
        """Add worklog to a Jira issue"""
        issue_key = validate_issue_key(issue_key)
        url = f"{self.base_url}/rest/api/2/issue/{issue_key}/worklog"
        
        payload = {
            "timeSpent": time_spent,
            "comment": comment
        }
        
        async with httpx.AsyncClient(verify=False) as client:
            try:
                response = await client.post(
                    url,
                    json=payload,
                    headers=self._get_headers(token)
                )
                
                if response.status_code not in [200, 201]:
                    raise JiraError(f"Worklog creation failed: {response.status_code} - {response.text}")
                
                data = response.json()
                
                return WorklogResult(
                    issue_key=issue_key,
                    time_spent=data['timeSpent'],
                    comment=data.get('comment', ''),
                    author=data['author']['displayName'],
                    created=data['created']
                )
                
            except httpx.RequestError as e:
                raise JiraError(f"Network error: {str(e)}")
    
    async def search_issues(self, token: str | None, jql: str, max_results: int = 50) -> SearchResult:
        """Search Jira issues using JQL"""
        url = f"{self.base_url}/rest/api/2/search"
        
        params = {
            "jql": jql,
            "maxResults": max_results,
            "fields": "summary,status,assignee,reporter,created,updated,description,issuetype,priority"
        }
        
        async with httpx.AsyncClient(verify=False) as client:
            try:
                response = await client.get(
                    url,
                    params=params,
                    headers=self._get_headers(token)
                )
                
                if response.status_code != 200:
                    raise JiraError(f"Search failed: {response.status_code} - {response.text}")
                
                data = response.json()
                
                issues = []
                for issue_data in data['issues']:
                    fields = issue_data['fields']
                    issues.append(JiraIssue(
                        key=issue_data['key'],
                        summary=fields['summary'],
                        status=fields['status']['name'],
                        assignee=fields['assignee']['displayName'] if fields['assignee'] else None,
                        reporter=fields['reporter']['displayName'],
                        created=fields['created'],
                        updated=fields['updated'],
                        description=fields.get('description', ''),
                        issue_type=fields['issuetype']['name'],
                        priority=fields['priority']['name']
                    ))
                
                return SearchResult(
                    total=data['total'],
                    issues=issues,
                    jql=jql
                )
                
            except httpx.RequestError as e:
                raise JiraError(f"Network error: {str(e)}")


async def serve(jira_base_url: str | None = None, default_token: str | None = None) -> None:
    server = Server("mcp-jira")
    jira_server = JiraServer(jira_base_url or "https://jira.telefonica.com.br", default_token)
    
    def get_token_description() -> str:
        """Get token description based on whether default token is configured"""
        if default_token:
            return "Jira Bearer token for authentication (optional - uses configured default if not provided)"
        return "Jira Bearer token for authentication"
    
    def get_required_fields(base_fields: list[str]) -> list[str]:
        """Get required fields, removing token if default is configured"""
        if default_token and "token" in base_fields:
            return [field for field in base_fields if field != "token"]
        return base_fields

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        """List available Jira tools."""
        return [
            Tool(
                name=JiraTools.GET_ISSUE.value,
                description="Get detailed information about a Jira issue",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "token": {
                            "type": "string",
                            "description": get_token_description()
                        },
                        "issue_key": {
                            "type": "string",
                            "description": "Jira issue key (e.g., 'LTC-4261', 'PROJ-123')"
                        }
                    },
                    "required": get_required_fields(["token", "issue_key"]),
                },
            ),
            Tool(
                name=JiraTools.GET_TRANSITIONS.value,
                description="Get available transitions for a Jira issue",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "token": {
                            "type": "string",
                            "description": get_token_description()
                        },
                        "issue_key": {
                            "type": "string",
                            "description": "Jira issue key (e.g., 'LTC-4261', 'PROJ-123')"
                        }
                    },
                    "required": get_required_fields(["token", "issue_key"]),
                },
            ),
            Tool(
                name=JiraTools.TRANSITION_ISSUE.value,
                description="Execute a transition on a Jira issue",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "token": {
                            "type": "string",
                            "description": get_token_description()
                        },
                        "issue_key": {
                            "type": "string",
                            "description": "Jira issue key (e.g., 'LTC-4261', 'PROJ-123')"
                        },
                        "transition_id": {
                            "type": "string",
                            "description": "ID of the transition to execute"
                        }
                    },
                    "required": get_required_fields(["token", "issue_key", "transition_id"]),
                },
            ),
            Tool(
                name=JiraTools.ADD_WORKLOG.value,
                description="Add worklog to a Jira issue",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "token": {
                            "type": "string",
                            "description": get_token_description()
                        },
                        "issue_key": {
                            "type": "string",
                            "description": "Jira issue key (e.g., 'LTC-4261', 'PROJ-123')"
                        },
                        "time_spent": {
                            "type": "string",
                            "description": "Time spent (e.g., '1h', '30m', '2h 30m')"
                        },
                        "comment": {
                            "type": "string",
                            "description": "Work description/comment (optional)"
                        }
                    },
                    "required": get_required_fields(["token", "issue_key", "time_spent"]),
                },
            ),
            Tool(
                name=JiraTools.SEARCH_ISSUES.value,
                description="Search Jira issues using JQL (Jira Query Language)",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "token": {
                            "type": "string",
                            "description": get_token_description()
                        },
                        "jql": {
                            "type": "string",
                            "description": "JQL query (e.g., 'assignee = currentUser() AND status = \"In Progress\"')"
                        },
                        "max_results": {
                            "type": "integer",
                            "description": "Maximum number of results to return (default: 50)",
                            "minimum": 1,
                            "maximum": 100
                        }
                    },
                    "required": get_required_fields(["token", "jql"]),
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(
        name: str, arguments: dict
    ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
        """Handle tool calls for Jira operations."""
        try:
            match name:
                case JiraTools.GET_ISSUE.value:
                    required_args = get_required_fields(["token", "issue_key"])
                    if not all(k in arguments for k in required_args):
                        raise ValueError(f"Missing required arguments: {', '.join(required_args)}")
                    
                    result = await jira_server.get_issue(
                        arguments.get("token"),
                        arguments["issue_key"]
                    )

                case JiraTools.GET_TRANSITIONS.value:
                    required_args = get_required_fields(["token", "issue_key"])
                    if not all(k in arguments for k in required_args):
                        raise ValueError(f"Missing required arguments: {', '.join(required_args)}")
                    
                    result = await jira_server.get_transitions(
                        arguments.get("token"),
                        arguments["issue_key"]
                    )

                case JiraTools.TRANSITION_ISSUE.value:
                    required_args = get_required_fields(["token", "issue_key", "transition_id"])
                    if not all(k in arguments for k in required_args):
                        raise ValueError(f"Missing required arguments: {', '.join(required_args)}")
                    
                    result = await jira_server.transition_issue(
                        arguments.get("token"),
                        arguments["issue_key"],
                        arguments["transition_id"]
                    )

                case JiraTools.ADD_WORKLOG.value:
                    required_args = get_required_fields(["token", "issue_key", "time_spent"])
                    if not all(k in arguments for k in required_args):
                        raise ValueError(f"Missing required arguments: {', '.join(required_args)}")
                    
                    result = await jira_server.add_worklog(
                        arguments.get("token"),
                        arguments["issue_key"],
                        arguments["time_spent"],
                        arguments.get("comment", "")
                    )

                case JiraTools.SEARCH_ISSUES.value:
                    required_args = get_required_fields(["token", "jql"])
                    if not all(k in arguments for k in required_args):
                        raise ValueError(f"Missing required arguments: {', '.join(required_args)}")
                    
                    result = await jira_server.search_issues(
                        arguments.get("token"),
                        arguments["jql"],
                        arguments.get("max_results", 50)
                    )

                case _:
                    raise ValueError(f"Unknown tool: {name}")

            return [
                TextContent(type="text", text=json.dumps(result.model_dump(), indent=2))
            ]

        except JiraError as e:
            error_msg = str(e) if hasattr(e, '__str__') else "Unknown Jira error"
            raise McpError(f"Jira operation failed: {error_msg}")
        except Exception as e:
            error_msg = str(e) if hasattr(e, '__str__') else f"Unknown error: {type(e).__name__}"
            raise McpError(f"Error processing Jira request: {error_msg}")

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options)