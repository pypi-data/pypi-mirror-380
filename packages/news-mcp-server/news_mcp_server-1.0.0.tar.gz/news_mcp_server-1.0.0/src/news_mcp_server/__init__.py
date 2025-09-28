"""
News MCP Server - Hybrid MCP server for news aggregation with Press Monitor integration.

This package provides a high-performance, caching-enabled MCP server that acts as
a proxy to news APIs while adding local enhancements and custom processing capabilities.
"""

__version__ = "1.0.0"
__author__ = "Your Organization"
__email__ = "dev@yourorg.com"

from .core.server import NewsMCPServer
from .core.config import Config
from .api.client import NewsMCPClient

__all__ = ["NewsMCPServer", "Config", "NewsMCPClient"]