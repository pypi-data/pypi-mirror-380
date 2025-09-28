"""Base plugin architecture for News MCP Server."""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type
from enum import Enum

from ..core.models import NewsResponse


logger = logging.getLogger(__name__)


class PluginType(str, Enum):
    """Plugin types."""
    FRAMEWORK_INTEGRATION = "framework_integration"
    CONTENT_PROCESSOR = "content_processor"
    DATA_ENHANCER = "data_enhancer"
    EXPORT_FORMAT = "export_format"
    AUTHENTICATION = "authentication"
    MONITORING = "monitoring"


@dataclass
class PluginMetadata:
    """Plugin metadata."""
    name: str
    version: str
    description: str
    author: str
    plugin_type: PluginType
    dependencies: List[str] = None
    config_schema: Optional[Dict[str, Any]] = None
    supported_formats: Optional[List[str]] = None

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []


class PluginConfig:
    """Plugin configuration wrapper."""

    def __init__(self, config_data: Optional[Dict[str, Any]] = None):
        self._config = config_data or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return self._config.copy()


class BasePlugin(ABC):
    """Base class for all plugins."""

    def __init__(self, config: Optional[PluginConfig] = None):
        self.config = config or PluginConfig()
        self._initialized = False
        self._enabled = True

    @property
    @abstractmethod
    def metadata(self) -> PluginMetadata:
        """Get plugin metadata."""
        pass

    @abstractmethod
    async def initialize(self) -> bool:
        """
        Initialize the plugin.

        Returns:
            bool: True if initialization successful, False otherwise
        """
        pass

    @abstractmethod
    async def shutdown(self) -> None:
        """Shutdown the plugin and cleanup resources."""
        pass

    async def validate_config(self) -> List[str]:
        """
        Validate plugin configuration.

        Returns:
            List[str]: List of validation errors, empty if valid
        """
        return []

    def is_enabled(self) -> bool:
        """Check if plugin is enabled."""
        return self._enabled

    def enable(self) -> None:
        """Enable the plugin."""
        self._enabled = True

    def disable(self) -> None:
        """Disable the plugin."""
        self._enabled = False

    def is_initialized(self) -> bool:
        """Check if plugin is initialized."""
        return self._initialized

    async def health_check(self) -> Dict[str, Any]:
        """
        Perform health check for the plugin.

        Returns:
            Dict containing health status
        """
        return {
            "status": "healthy" if self._enabled else "disabled",
            "initialized": self._initialized,
            "plugin": self.metadata.name,
            "version": self.metadata.version
        }


class FrameworkPlugin(BasePlugin):
    """Base class for AI framework integration plugins."""

    @abstractmethod
    async def create_tool(self, server_url: str, api_key: Optional[str] = None) -> Any:
        """
        Create a tool/component for the AI framework.

        Args:
            server_url: URL of the MCP server
            api_key: Optional API key for authentication

        Returns:
            Framework-specific tool object
        """
        pass

    @abstractmethod
    def get_example_usage(self) -> str:
        """
        Get example usage code for this framework.

        Returns:
            String containing example code
        """
        pass


class ContentProcessorPlugin(BasePlugin):
    """Base class for content processing plugins."""

    @abstractmethod
    async def process_news_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a single news item.

        Args:
            item: News item data

        Returns:
            Processed news item data
        """
        pass

    @abstractmethod
    async def process_news_response(self, response: NewsResponse) -> NewsResponse:
        """
        Process entire news response.

        Args:
            response: News response object

        Returns:
            Processed news response
        """
        pass


class DataEnhancerPlugin(BasePlugin):
    """Base class for data enhancement plugins."""

    @abstractmethod
    async def enhance_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enhance a news item with additional data.

        Args:
            item: Original news item

        Returns:
            Enhanced news item
        """
        pass

    @abstractmethod
    def get_enhancement_fields(self) -> List[str]:
        """
        Get list of fields this plugin adds/enhances.

        Returns:
            List of field names
        """
        pass


class ExportFormatPlugin(BasePlugin):
    """Base class for export format plugins."""

    @abstractmethod
    async def export_data(self, data: NewsResponse, options: Optional[Dict[str, Any]] = None) -> Any:
        """
        Export news data to specific format.

        Args:
            data: News response data
            options: Export options

        Returns:
            Exported data in target format
        """
        pass

    @abstractmethod
    def get_supported_formats(self) -> List[str]:
        """
        Get list of supported export formats.

        Returns:
            List of format names
        """
        pass

    @abstractmethod
    def get_mime_type(self, format_name: str) -> str:
        """
        Get MIME type for format.

        Args:
            format_name: Name of the format

        Returns:
            MIME type string
        """
        pass


class AuthenticationPlugin(BasePlugin):
    """Base class for authentication plugins."""

    @abstractmethod
    async def authenticate(self, credentials: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Authenticate user credentials.

        Args:
            credentials: User credentials

        Returns:
            User info if authenticated, None otherwise
        """
        pass

    @abstractmethod
    async def authorize(self, user_info: Dict[str, Any], resource: str, action: str) -> bool:
        """
        Check if user is authorized for action on resource.

        Args:
            user_info: Authenticated user information
            resource: Resource being accessed
            action: Action being performed

        Returns:
            True if authorized, False otherwise
        """
        pass


class MonitoringPlugin(BasePlugin):
    """Base class for monitoring plugins."""

    @abstractmethod
    async def collect_metrics(self) -> Dict[str, Any]:
        """
        Collect custom metrics.

        Returns:
            Dictionary of metrics
        """
        pass

    @abstractmethod
    async def send_alert(self, alert_type: str, message: str, metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Send an alert/notification.

        Args:
            alert_type: Type of alert
            message: Alert message
            metadata: Additional alert metadata

        Returns:
            True if alert sent successfully
        """
        pass


class PluginError(Exception):
    """Base exception for plugin errors."""
    pass


class PluginInitializationError(PluginError):
    """Plugin initialization error."""
    pass


class PluginConfigurationError(PluginError):
    """Plugin configuration error."""
    pass


class PluginDependencyError(PluginError):
    """Plugin dependency error."""
    pass