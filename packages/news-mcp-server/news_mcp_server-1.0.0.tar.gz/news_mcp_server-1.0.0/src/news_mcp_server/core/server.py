"""Main FastAPI server for News MCP Server."""

import asyncio
import time
import logging
from typing import Any, Dict, Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
import httpx

from .config import Config
from .models import (
    MCPRequest, MCPResponse, MCPError, NewsQuery,
    NewsHeadlinesResponse, NewsBriefsResponse, NewsFullTextResponse,
    NewsMetadataResponse, HealthStatus, MetricsData
)
from ..cache.manager import CacheManager
from ..monitoring.metrics import MetricsCollector
from ..monitoring.health import HealthChecker
from ..plugins.manager import PluginManager


logger = logging.getLogger(__name__)


class NewsMCPServer:
    """Main News MCP Server implementation."""

    def __init__(self, config: Config):
        self.config = config
        self.cache_manager = CacheManager(config.cache)
        self.metrics = MetricsCollector()
        self.health_checker = HealthChecker()
        self.plugin_manager = PluginManager()
        self.http_client: Optional[httpx.AsyncClient] = None
        self.app = self._create_app()

    def _create_app(self) -> FastAPI:
        """Create FastAPI application with middleware and routes."""

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            """Application lifespan management."""
            await self.startup()
            yield
            await self.shutdown()

        app = FastAPI(
            title="News MCP Server",
            description="Hybrid MCP server for news aggregation with Press Monitor integration",
            version="1.0.0",
            lifespan=lifespan
        )

        # Add CORS middleware
        if self.config.security.cors.enabled:
            app.add_middleware(
                CORSMiddleware,
                allow_origins=self.config.security.cors.allow_origins,
                allow_credentials=True,
                allow_methods=self.config.security.cors.allow_methods,
                allow_headers=self.config.security.cors.allow_headers,
            )

        # Add routes
        self._add_routes(app)

        return app

    def _add_routes(self, app: FastAPI) -> None:
        """Add all routes to the FastAPI app."""

        @app.middleware("http")
        async def metrics_middleware(request: Request, call_next):
            """Middleware to collect request metrics."""
            start_time = time.time()

            response = await call_next(request)

            duration = time.time() - start_time
            self.metrics.record_request(
                method=request.method,
                endpoint=str(request.url.path),
                status_code=response.status_code,
                duration=duration
            )

            return response

        @app.post("/mcp")
        async def mcp_endpoint(
            request: MCPRequest,
            api_key: Optional[str] = Header(None, alias="X-API-Key")
        ):
            """Main MCP JSON-RPC endpoint."""
            return await self._handle_mcp_request(request, api_key)

        @app.get("/health")
        async def health_check():
            """Health check endpoint."""
            health_status = await self.health_checker.check_health()
            return health_status.dict()

        @app.get("/metrics")
        async def metrics_endpoint():
            """Prometheus metrics endpoint."""
            metrics_data = await self.metrics.get_metrics()
            return PlainTextResponse(
                content=self.metrics.generate_prometheus_metrics(),
                media_type="text/plain"
            )

        @app.get("/")
        async def root():
            """Root endpoint with server information."""
            return {
                "name": "News MCP Server",
                "version": "1.0.0",
                "status": "running",
                "endpoints": {
                    "mcp": "/mcp",
                    "health": "/health",
                    "metrics": "/metrics"
                }
            }

    async def startup(self) -> None:
        """Initialize server components."""
        logger.info("Starting News MCP Server...")

        # Initialize HTTP client
        self.http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(self.config.news_apis.get("press_monitor", {}).get("timeout", 30)),
            follow_redirects=True
        )

        # Initialize cache
        await self.cache_manager.initialize()

        # Initialize monitoring
        await self.health_checker.initialize()

        # Initialize plugins
        await self.plugin_manager.initialize()

        logger.info("News MCP Server started successfully")

    async def shutdown(self) -> None:
        """Cleanup server components."""
        logger.info("Shutting down News MCP Server...")

        if self.http_client:
            await self.http_client.aclose()

        await self.cache_manager.close()
        await self.plugin_manager.shutdown()

        logger.info("News MCP Server shutdown complete")

    async def _handle_mcp_request(self, request: MCPRequest, api_key: Optional[str]) -> MCPResponse:
        """Handle MCP JSON-RPC requests."""
        try:
            # Validate API key if required
            if self.config.get_api_key() and api_key != self.config.get_api_key():
                return MCPResponse(
                    id=request.id,
                    error=MCPError(code=-32000, message="Invalid API key").dict()
                )

            # Route to appropriate handler
            if request.method == "news_headlines":
                result = await self._handle_news_headlines(request.params)
            elif request.method == "news_briefs":
                result = await self._handle_news_briefs(request.params)
            elif request.method == "news_fulltext":
                result = await self._handle_news_fulltext(request.params)
            elif request.method == "news_fulltext_metadata":
                result = await self._handle_news_metadata(request.params)
            elif request.method == "news_headlines_translated":
                result = await self._handle_news_headlines_translated(request.params)
            else:
                return MCPResponse(
                    id=request.id,
                    error=MCPError(code=-32601, message=f"Method not found: {request.method}").dict()
                )

            return MCPResponse(id=request.id, result=result)

        except Exception as e:
            logger.error(f"Error handling MCP request: {e}")
            return MCPResponse(
                id=request.id,
                error=MCPError(code=-32603, message=str(e)).dict()
            )

    async def _handle_news_headlines(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle news headlines requests."""
        query = NewsQuery(**params)
        cache_key = f"headlines:{hash(str(sorted(params.items())))}"

        # Check cache first
        if self.cache_manager.provider:
            cached_result = await self.cache_manager.get(cache_key)
            if cached_result:
                cached_result["cached"] = True
                return cached_result

        # Make request to Press Monitor API
        result = await self._make_press_monitor_request("news/headlines", query.dict())

        # Cache result
        if self.cache_manager.provider and result:
            await self.cache_manager.set(cache_key, result, ttl=self.config.cache.ttl)

        return result

    async def _handle_news_briefs(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle news briefs requests."""
        query = NewsQuery(**params)
        cache_key = f"briefs:{hash(str(sorted(params.items())))}"

        # Check cache first
        if self.cache_manager.provider:
            cached_result = await self.cache_manager.get(cache_key)
            if cached_result:
                cached_result["cached"] = True
                return cached_result

        # Make request to Press Monitor API
        result = await self._make_press_monitor_request("news/briefs", query.dict())

        # Cache result
        if self.cache_manager.provider and result:
            await self.cache_manager.set(cache_key, result, ttl=self.config.cache.ttl)

        return result

    async def _handle_news_fulltext(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle news fulltext requests."""
        query = NewsQuery(**params)
        cache_key = f"fulltext:{hash(str(sorted(params.items())))}"

        # Check cache first
        if self.cache_manager.provider:
            cached_result = await self.cache_manager.get(cache_key)
            if cached_result:
                cached_result["cached"] = True
                return cached_result

        # Make request to Press Monitor API
        result = await self._make_press_monitor_request("news/fulltext", query.dict())

        # Cache result
        if self.cache_manager.provider and result:
            await self.cache_manager.set(cache_key, result, ttl=self.config.cache.ttl)

        return result

    async def _handle_news_metadata(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle news metadata requests."""
        query = NewsQuery(**params)
        cache_key = f"metadata:{hash(str(sorted(params.items())))}"

        # Check cache first
        if self.cache_manager.provider:
            cached_result = await self.cache_manager.get(cache_key)
            if cached_result:
                cached_result["cached"] = True
                return cached_result

        # Make request to Press Monitor API
        result = await self._make_press_monitor_request("news/fulltext/metadata", query.dict())

        # Cache result
        if self.cache_manager.provider and result:
            await self.cache_manager.set(cache_key, result, ttl=self.config.cache.ttl)

        return result

    async def _handle_news_headlines_translated(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle translated news headlines requests."""
        query = NewsQuery(**params)
        cache_key = f"headlines_translated:{hash(str(sorted(params.items())))}"

        # Check cache first
        if self.cache_manager.provider:
            cached_result = await self.cache_manager.get(cache_key)
            if cached_result:
                cached_result["cached"] = True
                return cached_result

        # Make request to Press Monitor API
        result = await self._make_press_monitor_request("news/headlines/translated", query.dict())

        # Cache result
        if self.cache_manager.provider and result:
            await self.cache_manager.set(cache_key, result, ttl=self.config.cache.ttl)

        return result

    async def _make_press_monitor_request(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Make request to Press Monitor API."""
        if not self.http_client:
            raise HTTPException(status_code=500, message="HTTP client not initialized")

        auth_token = self.config.get_press_monitor_auth()
        if not auth_token:
            raise HTTPException(status_code=500, message="Press Monitor API key not configured")

        press_monitor_config = self.config.news_apis.get("press_monitor")
        if not press_monitor_config:
            raise HTTPException(status_code=500, message="Press Monitor configuration not found")

        url = f"{press_monitor_config.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }

        # Clean params - remove None values
        clean_params = {k: v for k, v in params.items() if v is not None}

        try:
            response = await self.http_client.post(url, json=clean_params, headers=headers)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            logger.error(f"Press Monitor API error: {e}")
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except Exception as e:
            logger.error(f"Request error: {e}")
            raise HTTPException(status_code=500, detail=str(e))


def create_app(config_path: Optional[str] = None) -> FastAPI:
    """Factory function to create FastAPI app."""
    from .config import load_config

    config = load_config(config_path)
    server = NewsMCPServer(config)
    return server.app