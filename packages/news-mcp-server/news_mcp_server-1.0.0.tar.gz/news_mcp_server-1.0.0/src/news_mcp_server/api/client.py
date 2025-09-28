"""Python SDK for News MCP Server."""

import asyncio
import logging
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import httpx
from pydantic import HttpUrl, ValidationError

from ..core.models import (
    NewsQuery,
    NewsHeadlinesResponse,
    NewsBriefsResponse,
    NewsFullTextResponse,
    NewsMetadataResponse,
    MCPRequest,
    MCPResponse,
)


logger = logging.getLogger(__name__)


class NewsMCPClientError(Exception):
    """Base exception for News MCP Client errors."""
    pass


class AuthenticationError(NewsMCPClientError):
    """Authentication related errors."""
    pass


class APIError(NewsMCPClientError):
    """API related errors."""
    pass


class NewsMCPClient:
    """Python client for News MCP Server."""

    def __init__(
        self,
        server_url: str = "http://localhost:3000",
        api_key: Optional[str] = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_delay: float = 1.0,
    ):
        """
        Initialize News MCP Client.

        Args:
            server_url: URL of the MCP server
            api_key: API key for authentication
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            retry_delay: Delay between retries in seconds
        """
        self.server_url = server_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        # HTTP client configuration
        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["X-API-Key"] = api_key

        self.client = httpx.AsyncClient(
            timeout=timeout,
            headers=headers,
            follow_redirects=True,
        )

        self._request_id_counter = 0

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self.client.aclose()

    def _get_next_request_id(self) -> str:
        """Get next request ID."""
        self._request_id_counter += 1
        return str(self._request_id_counter)

    async def _make_mcp_request(
        self,
        method: str,
        params: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Make MCP JSON-RPC request."""
        request_id = self._get_next_request_id()

        mcp_request = MCPRequest(
            id=request_id,
            method=method,
            params=params
        )

        for attempt in range(self.max_retries + 1):
            try:
                response = await self.client.post(
                    f"{self.server_url}/mcp",
                    json=mcp_request.dict(),
                )

                if response.status_code == 401:
                    raise AuthenticationError("Invalid API key")

                if response.status_code == 429:
                    raise APIError("Rate limit exceeded")

                response.raise_for_status()

                response_data = response.json()
                mcp_response = MCPResponse(**response_data)

                if mcp_response.error:
                    raise APIError(f"MCP Error: {mcp_response.error}")

                return mcp_response.result

            except httpx.HTTPStatusError as e:
                if attempt == self.max_retries:
                    raise APIError(f"HTTP error: {e}")

                if e.response.status_code < 500:
                    # Don't retry client errors
                    raise APIError(f"HTTP error: {e}")

                # Retry server errors
                logger.warning(f"Request failed (attempt {attempt + 1}), retrying...")
                await asyncio.sleep(self.retry_delay * (2 ** attempt))

            except httpx.RequestError as e:
                if attempt == self.max_retries:
                    raise APIError(f"Request error: {e}")

                logger.warning(f"Request failed (attempt {attempt + 1}), retrying...")
                await asyncio.sleep(self.retry_delay * (2 ** attempt))

        raise APIError("Max retries exceeded")

    async def get_headlines(
        self,
        query: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        search_after: Optional[str] = None,
    ) -> NewsHeadlinesResponse:
        """
        Get news headlines.

        Args:
            query: Search query text
            country_code: CSV of ISO-3166-1 alpha-2 country codes
            lang_code: CSV of ISO-639-1 language codes
            sort: Sort order ("latest" or "relevance")
            count: Number of results (1-100)
            search_after: Pagination cursor

        Returns:
            NewsHeadlinesResponse with headlines data
        """
        params = {
            "query_text": query,
            "sort": sort,
            "count": count,
        }

        if country_code:
            params["country_code"] = country_code
        if lang_code:
            params["lang_code"] = lang_code
        if search_after:
            params["search_after"] = search_after

        result = await self._make_mcp_request("news_headlines", params)
        return NewsHeadlinesResponse(**result)

    async def get_briefs(
        self,
        query: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        search_after: Optional[str] = None,
    ) -> NewsBriefsResponse:
        """
        Get news briefs with summaries.

        Args:
            query: Search query text
            country_code: CSV of ISO-3166-1 alpha-2 country codes
            lang_code: CSV of ISO-639-1 language codes
            sort: Sort order ("latest" or "relevance")
            count: Number of results (1-100)
            search_after: Pagination cursor

        Returns:
            NewsBriefsResponse with briefs data
        """
        params = {
            "query_text": query,
            "sort": sort,
            "count": count,
        }

        if country_code:
            params["country_code"] = country_code
        if lang_code:
            params["lang_code"] = lang_code
        if search_after:
            params["search_after"] = search_after

        result = await self._make_mcp_request("news_briefs", params)
        return NewsBriefsResponse(**result)

    async def get_fulltext(
        self,
        query: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        search_after: Optional[str] = None,
    ) -> NewsFullTextResponse:
        """
        Get full text news articles.

        Args:
            query: Search query text
            country_code: CSV of ISO-3166-1 alpha-2 country codes
            lang_code: CSV of ISO-639-1 language codes
            sort: Sort order ("latest" or "relevance")
            count: Number of results (1-100)
            search_after: Pagination cursor

        Returns:
            NewsFullTextResponse with full articles
        """
        params = {
            "query_text": query,
            "sort": sort,
            "count": count,
        }

        if country_code:
            params["country_code"] = country_code
        if lang_code:
            params["lang_code"] = lang_code
        if search_after:
            params["search_after"] = search_after

        result = await self._make_mcp_request("news_fulltext", params)
        return NewsFullTextResponse(**result)

    async def get_metadata(
        self,
        query: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        search_after: Optional[str] = None,
    ) -> NewsMetadataResponse:
        """
        Get news articles with enriched metadata.

        Args:
            query: Search query text
            country_code: CSV of ISO-3166-1 alpha-2 country codes
            lang_code: CSV of ISO-639-1 language codes
            sort: Sort order ("latest" or "relevance")
            count: Number of results (1-100)
            search_after: Pagination cursor

        Returns:
            NewsMetadataResponse with metadata-enriched articles
        """
        params = {
            "query_text": query,
            "sort": sort,
            "count": count,
        }

        if country_code:
            params["country_code"] = country_code
        if lang_code:
            params["lang_code"] = lang_code
        if search_after:
            params["search_after"] = search_after

        result = await self._make_mcp_request("news_fulltext_metadata", params)
        return NewsMetadataResponse(**result)

    async def get_headlines_translated(
        self,
        query: str,
        target_lang_code: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        search_after: Optional[str] = None,
    ) -> NewsHeadlinesResponse:
        """
        Get translated news headlines.

        Args:
            query: Search query text
            target_lang_code: Target language for translation (ISO-639-1)
            country_code: CSV of ISO-3166-1 alpha-2 country codes
            lang_code: CSV of ISO-639-1 language codes
            sort: Sort order ("latest" or "relevance")
            count: Number of results (1-100)
            search_after: Pagination cursor

        Returns:
            NewsHeadlinesResponse with translated headlines
        """
        params = {
            "query_text": query,
            "target_lang_code": target_lang_code,
            "sort": sort,
            "count": count,
        }

        if country_code:
            params["country_code"] = country_code
        if lang_code:
            params["lang_code"] = lang_code
        if search_after:
            params["search_after"] = search_after

        result = await self._make_mcp_request("news_headlines_translated", params)
        return NewsHeadlinesResponse(**result)

    async def health_check(self) -> Dict[str, Any]:
        """Check server health status."""
        try:
            response = await self.client.get(f"{self.server_url}/health")
            response.raise_for_status()
            return response.json()

        except Exception as e:
            raise APIError(f"Health check failed: {e}")

    async def get_metrics(self) -> Dict[str, Any]:
        """Get server metrics."""
        try:
            response = await self.client.get(f"{self.server_url}/metrics")
            response.raise_for_status()
            return response.json()

        except Exception as e:
            raise APIError(f"Failed to get metrics: {e}")


# Synchronous wrapper for convenience
class NewsMCPSyncClient:
    """Synchronous wrapper for NewsMCPClient."""

    def __init__(self, **kwargs):
        self._client = NewsMCPClient(**kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        asyncio.run(self._client.close())

    def get_headlines(self, **kwargs) -> NewsHeadlinesResponse:
        """Synchronous version of get_headlines."""
        return asyncio.run(self._client.get_headlines(**kwargs))

    def get_briefs(self, **kwargs) -> NewsBriefsResponse:
        """Synchronous version of get_briefs."""
        return asyncio.run(self._client.get_briefs(**kwargs))

    def get_fulltext(self, **kwargs) -> NewsFullTextResponse:
        """Synchronous version of get_fulltext."""
        return asyncio.run(self._client.get_fulltext(**kwargs))

    def get_metadata(self, **kwargs) -> NewsMetadataResponse:
        """Synchronous version of get_metadata."""
        return asyncio.run(self._client.get_metadata(**kwargs))

    def health_check(self) -> Dict[str, Any]:
        """Synchronous version of health_check."""
        return asyncio.run(self._client.health_check())

    def get_metrics(self) -> Dict[str, Any]:
        """Synchronous version of get_metrics."""
        return asyncio.run(self._client.get_metrics())