#!/usr/bin/env python3
"""
MCP (Model Context Protocol) Service for Ollama Web Search
This service implements a proper MCP server using the official Python SDK.
"""
import asyncio
import logging
import os
from typing import Any, Dict, List

import mcp.types as types
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from dotenv import load_dotenv
import ollama
from ollama import WebSearchResponse
from ollama._types import WebSearchResult

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create server instance
server = Server("ollama-web-search")

class OllamaSearchService:
    """A service to handle Ollama web search functionality."""

    def __init__(self, api_key: str = None):
        """
        Initialize the OllamaSearchService instance.

        Args:
            api_key (str, optional): Ollama API key. If not provided, it will be loaded from environment variables.
        """
        if api_key is None:
            api_key = os.environ.get("OLLAMA_API_KEY")
            if api_key is None:
                raise ValueError("OLLAMA_API_KEY environment variable not set. Please set it in your .env file.")
            if api_key == "your_api_key_here":
                raise ValueError("Please update your OLLAMA_API_KEY in the .env file with a valid API key.")

        self.api_key = api_key
        self.client = ollama.Client(
            host='https://ollama.com',
            headers={'Authorization': f'Bearer {self.api_key}'}
        )

    def search(self, query: str, max_results: int = 3) -> Dict[str, Any]:
        """
        Perform a web search using Ollama.

        Args:
            query (str): The search query.
            max_results (int): Maximum number of results to return (default: 3).

        Returns:
            dict: The search response from Ollama.
        """
        if not query or not isinstance(query, str):
            raise ValueError("Query must be a non-empty string")

        if not isinstance(max_results, int) or max_results < 1 or max_results > 100:
            raise ValueError("max_results must be an integer between 1 and 100")

        try:
            response = self.client.web_search(query, max_results)
            return {
                "success": True,
                "data": response,
                "query": query
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "query": query
            }

    def format_results(self, response: Dict[str, Any]) -> str:
        """
        Format search results into a readable string.

        Args:
            response (dict): The response from the search method.

        Returns:
            str: Formatted search results.
        """
        if not isinstance(response, dict):
            return "Error: Invalid response format"

        if not response.get("success", False):
            return f"Error: {response.get('error', 'Unknown error')}"

        data = response.get("data", {})
        if not isinstance(data, WebSearchResponse):
            return "Error: Invalid data format"

        results = data.get("results", [])
        if not isinstance(results, list):
            return "Error: Invalid results format"

        if not results:
            return "No results found."

        result = ''
        for i, item in enumerate(results, 1):
            if not isinstance(item, WebSearchResult):
                continue

            title = item.get('title', 'No title')
            url = item.get('url', 'No URL')
            content = item.get('content', 'No content')

            result += f"{i}. {title}\n"
            result += f"   URL: {url}\n"
            result += f"   Content: {content}\n\n"
        return result

    def search_and_format(self, query: str, max_results: int = 3) -> Dict[str, Any]:
        """
        Perform a search and return both raw and formatted results.

        Args:
            query (str): The search query.
            max_results (int): Maximum number of results to return (default: 3).

        Returns:
            dict: Search results with both raw data and formatted string.
        """
        response = self.search(query, max_results)
        if response["success"]:
            formatted = self.format_results(response)
            response["formatted"] = formatted
        return response


# Initialize the search service
try:
    search_service = OllamaSearchService()
except ValueError as e:
    logger.error(f"Error initializing service: {e}")
    search_service = None


@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="search",
            description="Perform a web search using Ollama",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 3, range: 1-10)",
                        "minimum": 1,
                        "maximum": 10
                    }
                },
                "required": ["query"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: Dict[str, Any] | None
) -> List[types.TextContent]:
    """Handle tool calls."""
    try:
        logger.info(f"Calling tool: {name} with arguments: {arguments}")

        if name == "search":
            if search_service is None:
                return [types.TextContent(
                    type="text",
                    text="Error: Service not initialized. Please check your OLLAMA_API_KEY."
                )]

            if not arguments or "query" not in arguments:
                return [types.TextContent(
                    type="text",
                    text="Error: 'query' parameter is required for search."
                )]

            query = arguments["query"]
            max_results = arguments.get("max_results", 3)

            response = search_service.search_and_format(query, max_results)

            if response["success"]:
                return [types.TextContent(
                    type="text",
                    text=response["formatted"]
                )]
            else:
                return [types.TextContent(
                    type="text",
                    text=f"Error: {response['error']}"
                )]

        else:
            return [types.TextContent(
                type="text",
                text=f"Error: Unknown tool '{name}'"
            )]

    except Exception as e:
        logger.error(f"Error calling tool {name}: {e}")
        return [types.TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Main function to run the MCP service."""
    try:
        # Run the server using stdio transport
        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="ollama-web-search",
                    server_version="0.1.0",
                    capabilities=server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )
    except Exception as e:
        logger.error(f"Error starting service: {e}")


def cli():
    """Command line interface entry point."""
    asyncio.run(main())


if __name__ == "__main__":
    # cli()
    response = search_service.search_and_format("What's Ollama?", max_results=2)
    print(response['formatted'])