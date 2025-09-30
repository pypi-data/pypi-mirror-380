"""Web Search Integration with multiple providers"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import aiohttp


@dataclass
class SearchResult:
    """Web search result"""

    title: str
    url: str
    snippet: str
    timestamp: datetime | None = None
    source: str = "web"
    metadata: dict[str, Any] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class WebSearchProvider(ABC):
    """Abstract web search provider"""

    @abstractmethod
    async def search(self, query: str, num_results: int = 5) -> list[SearchResult]:
        """Execute search and return results"""
        pass


class BraveSearchProvider(WebSearchProvider):
    """Brave Search API provider"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.search.brave.com/res/v1/web/search"

    async def search(self, query: str, num_results: int = 5) -> list[SearchResult]:
        """Search using Brave Search API"""
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": self.api_key,
        }

        params = {
            "q": query,
            "count": min(num_results, 20),  # Brave API limit
            "offset": 0,
            "mkt": "en-US",
            "safesearch": "moderate",
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self.base_url,
                    headers=headers,
                    params=params,
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as response:
                    if response.status != 200:
                        raise RuntimeError(f"Brave Search API error: {response.status}")

                    data = await response.json()
                    return self._parse_brave_results(data)

        except Exception as e:
            raise RuntimeError(f"Brave search failed: {str(e)}") from e

    def _parse_brave_results(self, data: dict[str, Any]) -> list[SearchResult]:
        """Parse Brave Search API response"""
        results = []
        web_results = data.get("web", {}).get("results", [])

        for result in web_results:
            search_result = SearchResult(
                title=result.get("title", ""),
                url=result.get("url", ""),
                snippet=result.get("description", ""),
                source="brave",
                metadata={
                    "age": result.get("age"),
                    "language": result.get("language"),
                    "family_friendly": result.get("family_friendly", True),
                },
            )
            results.append(search_result)

        return results


class GoogleSearchProvider(WebSearchProvider):
    """Google Custom Search API provider"""

    def __init__(self, api_key: str, cx: str):
        self.api_key = api_key
        self.cx = cx  # Custom Search Engine ID
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    async def search(self, query: str, num_results: int = 5) -> list[SearchResult]:
        """Search using Google Custom Search API"""
        params = {
            "key": self.api_key,
            "cx": self.cx,
            "q": query,
            "num": min(num_results, 10),  # Google API limit per request
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self.base_url,
                    params=params,
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as response:
                    if response.status != 200:
                        raise RuntimeError(
                            f"Google Search API error: {response.status}"
                        )

                    data = await response.json()
                    return self._parse_google_results(data)

        except Exception as e:
            raise RuntimeError(f"Google search failed: {str(e)}") from e

    def _parse_google_results(self, data: dict[str, Any]) -> list[SearchResult]:
        """Parse Google Custom Search API response"""
        results = []
        items = data.get("items", [])

        for item in items:
            search_result = SearchResult(
                title=item.get("title", ""),
                url=item.get("link", ""),
                snippet=item.get("snippet", ""),
                source="google",
                metadata={
                    "display_link": item.get("displayLink"),
                    "formatted_url": item.get("formattedUrl"),
                },
            )
            results.append(search_result)

        return results


class WebSearchClient:
    """Main web search client with multiple provider support"""

    def __init__(self, provider: WebSearchProvider):
        self.provider = provider
        self.session: aiohttp.ClientSession | None = None

    @classmethod
    def create_brave_client(cls, api_key: str) -> "WebSearchClient":
        """Create client with Brave Search provider"""
        return cls(BraveSearchProvider(api_key))

    @classmethod
    def create_google_client(cls, api_key: str, cx: str) -> "WebSearchClient":
        """Create client with Google Custom Search provider"""
        return cls(GoogleSearchProvider(api_key, cx))

    async def search(
        self, query: str, num_results: int = 5, filter_duplicates: bool = True
    ) -> list[SearchResult]:
        """Execute web search"""
        if not query or not query.strip():
            return []

        results = await self.provider.search(query.strip(), num_results)

        if filter_duplicates:
            results = self._remove_duplicates(results)

        return results

    async def fetch_content(self, url: str) -> str | None:
        """Fetch full content from a URL"""
        if not self.session:
            self.session = aiohttp.ClientSession()

        try:
            async with self.session.get(
                url,
                timeout=aiohttp.ClientTimeout(total=30),
                headers={"User-Agent": "AII-Bot/1.0 (https://github.com/aiiware/aii)"},
            ) as response:
                if response.status == 200:
                    content = await response.text()
                    return self._extract_text_content(content)
                return None

        except Exception as e:
            print(f"Error fetching content from {url}: {e}")
            return None

    async def search_and_fetch(
        self, query: str, num_results: int = 3, fetch_full_content: bool = False
    ) -> list[dict[str, Any]]:
        """Search and optionally fetch full content"""
        search_results = await self.search(query, num_results)

        if not fetch_full_content:
            return [
                {
                    "title": result.title,
                    "url": result.url,
                    "snippet": result.snippet,
                    "source": result.source,
                }
                for result in search_results
            ]

        # Fetch full content for each result
        enriched_results = []
        for result in search_results:
            full_content = await self.fetch_content(result.url)

            enriched_results.append(
                {
                    "title": result.title,
                    "url": result.url,
                    "snippet": result.snippet,
                    "full_content": full_content,
                    "source": result.source,
                    "metadata": result.metadata,
                }
            )

        return enriched_results

    async def close(self) -> None:
        """Close HTTP session"""
        if self.session:
            await self.session.close()
            self.session = None

    def _remove_duplicates(self, results: list[SearchResult]) -> list[SearchResult]:
        """Remove duplicate results based on URL"""
        seen_urls = set()
        unique_results = []

        for result in results:
            if result.url not in seen_urls:
                seen_urls.add(result.url)
                unique_results.append(result)

        return unique_results

    def _extract_text_content(self, html_content: str) -> str:
        """Extract readable text from HTML content"""
        # This is a simplified text extraction
        # In production, you'd want to use libraries like BeautifulSoup or readability
        try:
            # Remove common HTML tags and scripts
            import re

            # Remove script and style tags
            html_content = re.sub(
                r"<script.*?</script>",
                "",
                html_content,
                flags=re.DOTALL | re.IGNORECASE,
            )
            html_content = re.sub(
                r"<style.*?</style>", "", html_content, flags=re.DOTALL | re.IGNORECASE
            )

            # Remove HTML tags
            text = re.sub(r"<[^>]+>", "", html_content)

            # Clean up whitespace
            text = re.sub(r"\\s+", " ", text)
            text = text.strip()

            # Limit length
            if len(text) > 5000:
                text = text[:5000] + "..."

            return text

        except Exception:
            return (
                html_content[:1000] + "..."
                if len(html_content) > 1000
                else html_content
            )
