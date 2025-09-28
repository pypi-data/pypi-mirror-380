"""Plugin manager for News MCP Server."""

import asyncio
import logging
import importlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, Union

from .base import (
    BasePlugin,
    PluginType,
    PluginConfig,
    PluginError,
    PluginInitializationError,
    PluginDependencyError
)


logger = logging.getLogger(__name__)


class PluginManager:
    """Manages plugins for News MCP Server."""

    def __init__(self):
        self.plugins: Dict[str, BasePlugin] = {}
        self.plugin_configs: Dict[str, PluginConfig] = {}
        self._initialized = False

    async def initialize(self, config: Optional[Dict[str, Any]] = None) -> None:
        """Initialize plugin manager and load plugins."""
        if self._initialized:
            return

        logger.info("Initializing plugin manager")

        # Load configuration
        if config:
            self._load_plugin_configs(config)

        # Load built-in plugins
        await self._load_builtin_plugins()

        # Load external plugins
        await self._load_external_plugins()

        self._initialized = True
        logger.info(f"Plugin manager initialized with {len(self.plugins)} plugins")

    async def shutdown(self) -> None:
        """Shutdown all plugins."""
        logger.info("Shutting down plugin manager")

        # Shutdown all plugins in reverse order
        for plugin_name in reversed(list(self.plugins.keys())):
            plugin = self.plugins[plugin_name]
            try:
                await plugin.shutdown()
                logger.info(f"Plugin '{plugin_name}' shut down successfully")
            except Exception as e:
                logger.error(f"Error shutting down plugin '{plugin_name}': {e}")

        self.plugins.clear()
        self._initialized = False

    def _load_plugin_configs(self, config: Dict[str, Any]) -> None:
        """Load plugin configurations."""
        plugins_config = config.get("plugins", {})

        for plugin_name, plugin_config in plugins_config.items():
            self.plugin_configs[plugin_name] = PluginConfig(plugin_config)

    async def _load_builtin_plugins(self) -> None:
        """Load built-in plugins."""
        builtin_plugins = [
            ("langchain", "langchain.LangChainPlugin"),
            ("crewai", "crewai.CrewAIPlugin"),
            ("autogpt", "autogpt.AutoGPTPlugin"),
        ]

        for plugin_name, plugin_path in builtin_plugins:
            try:
                await self._load_plugin(plugin_name, plugin_path, builtin=True)
            except Exception as e:
                logger.warning(f"Failed to load built-in plugin '{plugin_name}': {e}")

    async def _load_external_plugins(self) -> None:
        """Load external plugins from plugins directory."""
        plugins_dir = Path(__file__).parent / "external"

        if not plugins_dir.exists():
            return

        for plugin_file in plugins_dir.glob("*.py"):
            if plugin_file.name.startswith("_"):
                continue

            plugin_name = plugin_file.stem
            try:
                await self._load_plugin_from_file(plugin_name, plugin_file)
            except Exception as e:
                logger.warning(f"Failed to load external plugin '{plugin_name}': {e}")

    async def _load_plugin(self, plugin_name: str, plugin_path: str, builtin: bool = False) -> None:
        """Load a plugin by name and path."""
        try:
            # Import plugin module
            if builtin:
                module_name = f"news_mcp_server.plugins.{plugin_path.split('.')[0]}"
                class_name = plugin_path.split('.')[-1]
            else:
                module_name = plugin_path
                class_name = "Plugin"

            module = importlib.import_module(module_name)
            plugin_class = getattr(module, class_name)

            # Get plugin configuration
            plugin_config = self.plugin_configs.get(plugin_name, PluginConfig())

            # Create plugin instance
            plugin = plugin_class(plugin_config)

            # Validate configuration
            validation_errors = await plugin.validate_config()
            if validation_errors:
                raise PluginError(f"Configuration validation failed: {validation_errors}")

            # Initialize plugin
            if await plugin.initialize():
                self.plugins[plugin_name] = plugin
                logger.info(f"Plugin '{plugin_name}' loaded successfully")
            else:
                raise PluginInitializationError(f"Plugin '{plugin_name}' initialization failed")

        except ImportError as e:
            # Don't fail for optional framework plugins
            if builtin and any(framework in str(e) for framework in ["langchain", "crewai", "autogpt"]):
                logger.debug(f"Optional framework not available for plugin '{plugin_name}': {e}")
            else:
                raise PluginDependencyError(f"Failed to import plugin '{plugin_name}': {e}")

    async def _load_plugin_from_file(self, plugin_name: str, plugin_file: Path) -> None:
        """Load a plugin from a Python file."""
        import importlib.util

        # Load module from file
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_file)
        if spec is None or spec.loader is None:
            raise PluginError(f"Cannot load plugin from {plugin_file}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Find plugin class
        plugin_class = None
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (isinstance(attr, type) and
                issubclass(attr, BasePlugin) and
                attr != BasePlugin):
                plugin_class = attr
                break

        if plugin_class is None:
            raise PluginError(f"No plugin class found in {plugin_file}")

        # Create and initialize plugin
        plugin_config = self.plugin_configs.get(plugin_name, PluginConfig())
        plugin = plugin_class(plugin_config)

        if await plugin.initialize():
            self.plugins[plugin_name] = plugin
            logger.info(f"External plugin '{plugin_name}' loaded from {plugin_file}")
        else:
            raise PluginInitializationError(f"Plugin '{plugin_name}' initialization failed")

    def get_plugin(self, plugin_name: str) -> Optional[BasePlugin]:
        """Get a plugin by name."""
        return self.plugins.get(plugin_name)

    def get_plugins_by_type(self, plugin_type: PluginType) -> List[BasePlugin]:
        """Get all plugins of a specific type."""
        return [
            plugin for plugin in self.plugins.values()
            if plugin.metadata.plugin_type == plugin_type and plugin.is_enabled()
        ]

    def list_plugins(self) -> Dict[str, Dict[str, Any]]:
        """List all loaded plugins with their metadata."""
        return {
            name: {
                "metadata": plugin.metadata.__dict__,
                "enabled": plugin.is_enabled(),
                "initialized": plugin.is_initialized()
            }
            for name, plugin in self.plugins.items()
        }

    async def enable_plugin(self, plugin_name: str) -> bool:
        """Enable a plugin."""
        plugin = self.plugins.get(plugin_name)
        if not plugin:
            return False

        plugin.enable()
        logger.info(f"Plugin '{plugin_name}' enabled")
        return True

    async def disable_plugin(self, plugin_name: str) -> bool:
        """Disable a plugin."""
        plugin = self.plugins.get(plugin_name)
        if not plugin:
            return False

        plugin.disable()
        logger.info(f"Plugin '{plugin_name}' disabled")
        return True

    async def reload_plugin(self, plugin_name: str) -> bool:
        """Reload a plugin."""
        plugin = self.plugins.get(plugin_name)
        if not plugin:
            return False

        try:
            # Shutdown current plugin
            await plugin.shutdown()

            # Get plugin configuration
            plugin_config = self.plugin_configs.get(plugin_name, PluginConfig())

            # Create new instance
            plugin_class = type(plugin)
            new_plugin = plugin_class(plugin_config)

            # Initialize new plugin
            if await new_plugin.initialize():
                self.plugins[plugin_name] = new_plugin
                logger.info(f"Plugin '{plugin_name}' reloaded successfully")
                return True
            else:
                # Restore old plugin if reload fails
                self.plugins[plugin_name] = plugin
                await plugin.initialize()
                return False

        except Exception as e:
            logger.error(f"Failed to reload plugin '{plugin_name}': {e}")
            return False

    async def health_check(self) -> Dict[str, Any]:
        """Perform health check on all plugins."""
        health_status = {
            "status": "healthy",
            "total_plugins": len(self.plugins),
            "enabled_plugins": len([p for p in self.plugins.values() if p.is_enabled()]),
            "plugins": {}
        }

        unhealthy_count = 0

        for name, plugin in self.plugins.items():
            try:
                plugin_health = await plugin.health_check()
                health_status["plugins"][name] = plugin_health

                if plugin_health.get("status") != "healthy":
                    unhealthy_count += 1

            except Exception as e:
                health_status["plugins"][name] = {
                    "status": "error",
                    "error": str(e)
                }
                unhealthy_count += 1

        if unhealthy_count > 0:
            health_status["status"] = "degraded" if unhealthy_count < len(self.plugins) else "unhealthy"

        return health_status

    async def get_framework_integrations(self) -> Dict[str, Any]:
        """Get available framework integrations."""
        framework_plugins = self.get_plugins_by_type(PluginType.FRAMEWORK_INTEGRATION)

        integrations = {}
        for plugin in framework_plugins:
            try:
                integrations[plugin.metadata.name] = {
                    "available": True,
                    "version": plugin.metadata.version,
                    "description": plugin.metadata.description,
                    "example_usage": plugin.get_example_usage() if hasattr(plugin, 'get_example_usage') else None
                }
            except Exception as e:
                integrations[plugin.metadata.name] = {
                    "available": False,
                    "error": str(e)
                }

        return integrations

    async def create_framework_tool(self, framework: str, server_url: str, api_key: Optional[str] = None) -> Any:
        """Create a tool for a specific framework."""
        plugin = self.get_plugin(framework)
        if not plugin:
            raise PluginError(f"Framework plugin '{framework}' not found")

        if not hasattr(plugin, 'create_tool'):
            raise PluginError(f"Plugin '{framework}' does not support tool creation")

        return await plugin.create_tool(server_url, api_key)

    def get_plugin_stats(self) -> Dict[str, Any]:
        """Get plugin statistics."""
        stats = {
            "total": len(self.plugins),
            "enabled": 0,
            "disabled": 0,
            "by_type": {}
        }

        for plugin in self.plugins.values():
            if plugin.is_enabled():
                stats["enabled"] += 1
            else:
                stats["disabled"] += 1

            plugin_type = plugin.metadata.plugin_type.value
            stats["by_type"][plugin_type] = stats["by_type"].get(plugin_type, 0) + 1

        return stats