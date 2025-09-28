"""Data models for News MCP Server."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, HttpUrl


class SortOption(str, Enum):
    """Sort options for news queries."""
    RELEVANCE = "relevance"
    LATEST = "latest"


class NewsSource(BaseModel):
    """News source information."""
    sitename: str
    domain: Optional[str] = None
    country_code: Optional[str] = None


class TranslationInfo(BaseModel):
    """Translation information."""
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    body: Optional[str] = None
    source_lang_code: str
    target_lang_code: str


class NewsItem(BaseModel):
    """Basic news item model."""
    id: str
    title: str
    url: HttpUrl
    source: str
    lang_code: str
    country_code: str
    ts: int
    first_source: Optional[NewsSource] = None

    @property
    def published_at(self) -> datetime:
        """Get published datetime from timestamp."""
        return datetime.fromtimestamp(self.ts)


class NewsBriefItem(NewsItem):
    """News brief with description."""
    description: Optional[str] = None
    images: List[HttpUrl] = []
    caption: Optional[str] = None


class NewsFullItem(NewsBriefItem):
    """Full news item with body."""
    body: Optional[str] = None


class NewsMetadataItem(NewsFullItem):
    """News item with enriched metadata."""
    wikidata: Optional[Dict[str, Any]] = None
    entities: List[Dict[str, Any]] = []
    mediatopics: List[str] = []


class TranslatedNewsItem(BaseModel):
    """News item with translations."""
    tr: TranslationInfo


class NewsQuery(BaseModel):
    """News search query parameters."""
    query_text: str = Field(..., description="Search query text")
    country_code: Optional[str] = Field(None, description="CSV of ISO-3166-1 alpha-2 country codes")
    lang_code: Optional[str] = Field(None, description="CSV of ISO-639-1 language codes")
    search_after: Optional[str] = Field(None, description="Pagination cursor")
    sort: SortOption = Field(SortOption.LATEST, description="Sort order")
    count: int = Field(20, ge=1, le=100, description="Number of results")
    target_lang_code: Optional[str] = Field(None, description="Target language for translation")


class CreditInfo(BaseModel):
    """API credit usage information."""
    rate: int = Field(description="Credits per item")
    quantity: int = Field(description="Number of items returned")
    total: int = Field(description="Credits used for this request")
    request_id: str = Field(description="Request identifier")


class PaginationInfo(BaseModel):
    """Pagination information."""
    search_after: Optional[str] = None
    count: int = 20
    sort: SortOption = SortOption.LATEST


class NewsResponse(BaseModel):
    """Base news response model."""
    items: List[NewsItem] = []
    credits: Optional[CreditInfo] = None
    next: Optional[PaginationInfo] = None
    cached: bool = Field(False, description="Whether response was served from cache")
    cache_ttl: Optional[int] = Field(None, description="Cache TTL in seconds")
    processing_time: Optional[float] = Field(None, description="Processing time in seconds")


class NewsHeadlinesResponse(NewsResponse):
    """News headlines response."""
    items: List[NewsItem] = []


class NewsBriefsResponse(NewsResponse):
    """News briefs response."""
    items: List[NewsBriefItem] = []


class NewsFullTextResponse(NewsResponse):
    """Full text news response."""
    items: List[NewsFullItem] = []


class NewsMetadataResponse(NewsResponse):
    """News metadata response."""
    items: List[NewsMetadataItem] = []


class MCPRequest(BaseModel):
    """MCP JSON-RPC request."""
    jsonrpc: str = "2.0"
    id: Union[str, int]
    method: str
    params: Dict[str, Any]


class MCPResponse(BaseModel):
    """MCP JSON-RPC response."""
    jsonrpc: str = "2.0"
    id: Union[str, int]
    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None


class MCPError(BaseModel):
    """MCP error response."""
    code: int
    message: str
    data: Optional[Any] = None


class HealthStatus(BaseModel):
    """Health check status."""
    status: str = Field(description="Overall health status")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    services: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    version: str = "1.0.0"


class MetricsData(BaseModel):
    """Metrics data model."""
    requests_total: int = 0
    requests_cached: int = 0
    cache_hit_rate: float = 0.0
    average_response_time: float = 0.0
    errors_total: int = 0
    active_connections: int = 0
    uptime_seconds: float = 0.0