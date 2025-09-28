"""Plugin framework for News MCP Server."""

from .manager import PluginManager
from .base import BasePlugin, PluginMetadata
from .langchain import LangChainPlugin
from .crewai import CrewAIPlugin
from .autogpt import AutoGPTPlugin

__all__ = [
    "PluginManager",
    "BasePlugin",
    "PluginMetadata",
    "LangChainPlugin",
    "CrewAIPlugin",
    "AutoGPTPlugin"
]