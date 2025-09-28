"""Configuration management for News MCP Server."""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, validator
from pydantic_settings import BaseSettings


class ServerConfig(BaseModel):
    """Server configuration."""
    host: str = "0.0.0.0"
    port: int = 3000
    reload: bool = False
    log_level: str = "info"


class NewsAPIConfig(BaseModel):
    """News API configuration."""
    base_url: str
    auth_type: str = "bearer"
    rate_limit: str = "100/hour"
    timeout: int = 30
    retry_attempts: int = 3
    retry_delay: float = 1.0


class CacheConfig(BaseModel):
    """Cache configuration."""
    provider: str = "redis"
    redis_url: str = "redis://localhost:6379/0"
    ttl: int = 300
    max_connections: int = 10
    enabled: bool = True


class MonitoringConfig(BaseModel):
    """Monitoring configuration."""
    enabled: bool = True
    metrics_endpoint: str = "/metrics"
    health_endpoint: str = "/health"
    prometheus_port: int = 9090


class RateLimitConfig(BaseModel):
    """Rate limiting configuration."""
    enabled: bool = True
    requests_per_minute: int = 60
    burst_limit: int = 100


class CORSConfig(BaseModel):
    """CORS configuration."""
    enabled: bool = True
    allow_origins: List[str] = ["*"]
    allow_methods: List[str] = ["GET", "POST", "OPTIONS"]
    allow_headers: List[str] = ["*"]


class SecurityConfig(BaseModel):
    """Security configuration."""
    api_key_header: str = "X-API-Key"
    rate_limiting: RateLimitConfig = RateLimitConfig()
    cors: CORSConfig = CORSConfig()


class CustomProcessingConfig(BaseModel):
    """Custom processing features configuration."""
    sentiment_analysis: bool = False
    content_summarization: bool = False
    entity_extraction: bool = False


class LocalEnhancementsConfig(BaseModel):
    """Local enhancements configuration."""
    duplicate_detection: bool = True
    content_filtering: bool = True
    trending_analysis: bool = False


class FeaturesConfig(BaseModel):
    """Features configuration."""
    custom_processing: CustomProcessingConfig = CustomProcessingConfig()
    local_enhancements: LocalEnhancementsConfig = LocalEnhancementsConfig()


class LoggingConfig(BaseModel):
    """Logging configuration."""
    level: str = "INFO"
    format: str = "json"
    file: Optional[str] = None
    max_size: str = "10MB"
    backup_count: int = 5


class Config(BaseSettings):
    """Main configuration class."""

    server: ServerConfig = ServerConfig()
    news_apis: Dict[str, NewsAPIConfig] = {}
    cache: CacheConfig = CacheConfig()
    monitoring: MonitoringConfig = MonitoringConfig()
    security: SecurityConfig = SecurityConfig()
    features: FeaturesConfig = FeaturesConfig()
    logging: LoggingConfig = LoggingConfig()

    # Environment variables
    press_monitor_api_key: Optional[str] = Field(None, env="PRESS_MONITOR_API_KEY")
    redis_url: Optional[str] = Field(None, env="REDIS_URL")
    api_key: Optional[str] = Field(None, env="NEWS_MCP_API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @classmethod
    def from_file(cls, config_path: Union[str, Path]) -> "Config":
        """Load configuration from JSON file."""
        config_path = Path(config_path)

        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

        with open(config_path, "r", encoding="utf-8") as f:
            config_data = json.load(f)

        # Override with environment variables
        if redis_url := os.getenv("REDIS_URL"):
            config_data.setdefault("cache", {})["redis_url"] = redis_url

        if press_monitor_key := os.getenv("PRESS_MONITOR_API_KEY"):
            config_data.setdefault("news_apis", {}).setdefault("press_monitor", {})
            # Store API key for later use, don't put in base config

        return cls(**config_data)

    def get_press_monitor_auth(self) -> Optional[str]:
        """Get Press Monitor authentication token."""
        return self.press_monitor_api_key or os.getenv("PRESS_MONITOR_API_KEY")

    def get_api_key(self) -> Optional[str]:
        """Get server API key for client authentication."""
        return self.api_key or os.getenv("NEWS_MCP_API_KEY")

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return self.dict()

    def validate_config(self) -> List[str]:
        """Validate configuration and return list of issues."""
        issues = []

        if not self.get_press_monitor_auth():
            issues.append("Press Monitor API key is required but not provided")

        if self.cache.enabled and self.cache.provider == "redis":
            redis_url = self.redis_url or self.cache.redis_url
            if not redis_url:
                issues.append("Redis URL is required when cache is enabled")

        if self.server.port < 1 or self.server.port > 65535:
            issues.append(f"Invalid server port: {self.server.port}")

        return issues


def load_config(config_path: Optional[str] = None) -> Config:
    """Load configuration from file or environment."""
    if config_path:
        return Config.from_file(config_path)

    # Try to find config file in common locations
    search_paths = [
        Path("config.json"),
        Path("config/config.json"),
        Path("/etc/news-mcp-server/config.json"),
    ]

    for path in search_paths:
        if path.exists():
            return Config.from_file(path)

    # Fall back to environment-only configuration
    return Config()