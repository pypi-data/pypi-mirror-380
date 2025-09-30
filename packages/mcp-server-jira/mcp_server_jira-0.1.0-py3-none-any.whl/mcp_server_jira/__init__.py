from .server import serve


def main():
    """MCP Jira Server - Jira integration functionality for MCP"""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="Give a model the ability to interact with Jira issues, transitions, and worklogs"
    )
    parser.add_argument(
        "--jira-base-url", 
        type=str, 
        help="Jira base URL (default: https://jira.telefonica.com.br)"
    )
    parser.add_argument(
        "--jira-token",
        type=str,
        help="Jira Bearer token for authentication (optional - can also be provided per request)"
    )

    args = parser.parse_args()
    asyncio.run(serve(args.jira_base_url, args.jira_token))


if __name__ == "__main__":
    main()