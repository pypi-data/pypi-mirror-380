"""External integrations"""

from .mcp_client import MCPClient, MCPResult
from .web_search import SearchResult, WebSearchClient

__all__ = ["WebSearchClient", "SearchResult", "MCPClient", "MCPResult"]
