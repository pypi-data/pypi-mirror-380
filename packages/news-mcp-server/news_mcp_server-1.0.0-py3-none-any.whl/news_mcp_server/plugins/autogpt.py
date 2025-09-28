"""AutoGPT integration plugin for News MCP Server."""

import logging
from typing import Any, Dict, List, Optional

from .base import FrameworkPlugin, PluginMetadata, PluginType, PluginConfig


logger = logging.getLogger(__name__)


class AutoGPTPlugin(FrameworkPlugin):
    """AutoGPT framework integration plugin."""

    def __init__(self, config: Optional[PluginConfig] = None):
        super().__init__(config)

    @property
    def metadata(self) -> PluginMetadata:
        """Get plugin metadata."""
        return PluginMetadata(
            name="autogpt-integration",
            version="1.0.0",
            description="AutoGPT framework integration for News MCP Server",
            author="News MCP Team",
            plugin_type=PluginType.FRAMEWORK_INTEGRATION,
            dependencies=["autogpt", "autogpt-forge"],
            supported_formats=["command", "plugin"]
        )

    async def initialize(self) -> bool:
        """Initialize AutoGPT plugin."""
        try:
            # Check if AutoGPT components are available
            self._autogpt_available = False
            try:
                # Try different AutoGPT import patterns
                import autogpt
                logger.info("AutoGPT detected")
                self._autogpt_available = True
            except ImportError:
                try:
                    from forge.sdk import Agent
                    logger.info("AutoGPT Forge detected")
                    self._autogpt_available = True
                except ImportError:
                    logger.warning("AutoGPT not installed. Plugin will provide installation instructions.")

            self._initialized = True
            logger.info("AutoGPT plugin initialized successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to initialize AutoGPT plugin: {e}")
            return False

    async def shutdown(self) -> None:
        """Shutdown AutoGPT plugin."""
        logger.info("AutoGPT plugin shutting down")

    async def create_tool(self, server_url: str, api_key: Optional[str] = None) -> Any:
        """Create AutoGPT command for News MCP Server."""
        if not self._autogpt_available:
            raise ImportError("AutoGPT is not installed. Install with: pip install autogpt")

        import httpx
        import json
        from typing import Dict, Any

        class NewsMCPCommand:
            """AutoGPT command for News MCP Server."""

            def __init__(self, server_url: str, api_key: Optional[str] = None):
                self.server_url = server_url
                self.api_key = api_key

            @property
            def name(self) -> str:
                return "news_search"

            @property
            def description(self) -> str:
                return "Search for news articles using the News MCP Server"

            @property
            def parameters(self) -> Dict[str, Any]:
                return {
                    "query": {
                        "type": "string",
                        "description": "Search query for news articles",
                        "required": True
                    },
                    "news_type": {
                        "type": "string",
                        "description": "Type of news data",
                        "enum": ["headlines", "briefs", "fulltext", "metadata"],
                        "default": "briefs"
                    },
                    "country_code": {
                        "type": "string",
                        "description": "Country codes (e.g., 'US', 'CA')",
                        "required": False
                    },
                    "lang_code": {
                        "type": "string",
                        "description": "Language codes (e.g., 'en', 'es')",
                        "required": False
                    },
                    "count": {
                        "type": "integer",
                        "description": "Number of articles to return",
                        "minimum": 1,
                        "maximum": 100,
                        "default": 10
                    }
                }

            async def execute(self, **kwargs) -> Dict[str, Any]:
                """Execute the news search command."""
                try:
                    query = kwargs.get("query")
                    if not query:
                        return {
                            "success": False,
                            "error": "Query parameter is required"
                        }

                    news_type = kwargs.get("news_type", "briefs")
                    country_code = kwargs.get("country_code")
                    lang_code = kwargs.get("lang_code")
                    count = kwargs.get("count", 10)

                    # Prepare MCP request
                    mcp_method = f"news_{news_type}"
                    mcp_params = {
                        "query_text": query,
                        "count": min(count, 100)
                    }

                    if country_code:
                        mcp_params["country_code"] = country_code
                    if lang_code:
                        mcp_params["lang_code"] = lang_code

                    mcp_request = {
                        "jsonrpc": "2.0",
                        "id": "1",
                        "method": mcp_method,
                        "params": mcp_params
                    }

                    # Make request
                    headers = {"Content-Type": "application/json"}
                    if self.api_key:
                        headers["X-API-Key"] = self.api_key

                    async with httpx.AsyncClient() as client:
                        response = await client.post(
                            f"{self.server_url}/mcp",
                            json=mcp_request,
                            headers=headers,
                            timeout=30.0
                        )
                        response.raise_for_status()

                        result = response.json()
                        if result.get("error"):
                            return {
                                "success": False,
                                "error": result["error"]["message"]
                            }

                        # Format response for AutoGPT
                        news_data = result.get("result", {})
                        items = news_data.get("items", [])

                        # Create structured response
                        formatted_articles = []
                        for item in items:
                            article = {
                                "title": item.get("title", ""),
                                "source": item.get("source", ""),
                                "url": item.get("url", ""),
                                "timestamp": item.get("ts", 0),
                                "country": item.get("country_code", ""),
                                "language": item.get("lang_code", "")
                            }

                            if "description" in item:
                                article["summary"] = item["description"]

                            if "body" in item:
                                article["content"] = item["body"]

                            if "entities" in item:
                                article["entities"] = item["entities"]

                            if "mediatopics" in item:
                                article["topics"] = item["mediatopics"]

                            formatted_articles.append(article)

                        return {
                            "success": True,
                            "data": {
                                "query": query,
                                "articles": formatted_articles,
                                "total_found": len(formatted_articles),
                                "news_type": news_type,
                                "credits_used": news_data.get("credits", {}).get("quantity", 0)
                            }
                        }

                except Exception as e:
                    return {
                        "success": False,
                        "error": f"Error executing news search: {str(e)}"
                    }

        return NewsMCPCommand(server_url, api_key)

    def get_example_usage(self) -> str:
        """Get example usage code."""
        return '''
# AutoGPT Integration Example

from autogpt import Agent
from news_mcp_server.plugins import AutoGPTPlugin

# Initialize plugin
plugin = AutoGPTPlugin()
await plugin.initialize()

# Create news search command
news_command = await plugin.create_tool(
    server_url="http://localhost:3000",
    api_key="your-api-key"
)

# Register command with AutoGPT agent
agent = Agent()
agent.register_command(news_command)

# Example usage in AutoGPT
# The agent can now use the news_search command:

# Command: news_search
# Parameters:
# {
#     "query": "artificial intelligence breakthrough",
#     "news_type": "fulltext",
#     "country_code": "US",
#     "count": 5
# }

# Or use the Forge SDK approach:
from forge.sdk import Agent, ForgeLogger

LOG = ForgeLogger(__name__)

class NewsResearchAgent(Agent):
    """
    An agent that specializes in news research and analysis.
    """

    def __init__(self):
        super().__init__()
        # Initialize news command
        self.news_command = None

    async def setup(self):
        """Setup the agent with news capabilities."""
        plugin = AutoGPTPlugin()
        await plugin.initialize()

        self.news_command = await plugin.create_tool(
            server_url="http://localhost:3000",
            api_key="your-api-key"
        )

    async def execute_step(self, task_id: str, step_request: dict) -> dict:
        """Execute a step in the task."""

        # Example: Search for news based on task requirements
        if "search news" in step_request.get("input", "").lower():
            query = self.extract_query_from_input(step_request["input"])

            result = await self.news_command.execute(
                query=query,
                news_type="briefs",
                count=10
            )

            if result["success"]:
                articles = result["data"]["articles"]
                summary = self.summarize_articles(articles)

                return {
                    "output": summary,
                    "additional_output": {
                        "articles_found": len(articles),
                        "raw_data": articles
                    }
                }
            else:
                return {"output": f"Failed to search news: {result['error']}"}

        return {"output": "No news search requested"}

    def extract_query_from_input(self, input_text: str) -> str:
        """Extract search query from user input."""
        # Simple extraction - in practice, use NLP
        words = input_text.lower().split()
        if "about" in words:
            idx = words.index("about") + 1
            return " ".join(words[idx:])
        return input_text

    def summarize_articles(self, articles: list) -> str:
        """Create a summary of articles."""
        if not articles:
            return "No articles found."

        summary = f"Found {len(articles)} relevant articles:\\n\\n"

        for i, article in enumerate(articles[:5], 1):
            summary += f"{i}. {article['title']}\\n"
            summary += f"   Source: {article['source']}\\n"
            if article.get('summary'):
                summary += f"   Summary: {article['summary'][:150]}...\\n"
            summary += "\\n"

        return summary

# Usage
agent = NewsResearchAgent()
await agent.setup()
'''

    def create_plugin_config(self) -> str:
        """Create AutoGPT plugin configuration."""
        return '''
# AutoGPT Plugin Configuration for News MCP

# Place this in your AutoGPT plugins directory

class NewsMCPPlugin:
    """AutoGPT plugin for News MCP Server integration."""

    def __init__(self):
        self.name = "news-mcp-plugin"
        self.version = "1.0.0"
        self.description = "Integration with News MCP Server for news research"

    def can_handle(self, message: str) -> bool:
        """Check if this plugin can handle the message."""
        news_keywords = [
            "news", "article", "headline", "breaking", "story",
            "current events", "latest", "recent", "update"
        ]
        return any(keyword in message.lower() for keyword in news_keywords)

    async def handle(self, message: str, context: dict) -> str:
        """Handle the news-related request."""
        from news_mcp_server.plugins import AutoGPTPlugin

        plugin = AutoGPTPlugin()
        await plugin.initialize()

        command = await plugin.create_tool(
            server_url=context.get("news_mcp_url", "http://localhost:3000"),
            api_key=context.get("news_mcp_api_key")
        )

        # Extract query from message
        query = self.extract_query(message)

        result = await command.execute(
            query=query,
            news_type="briefs",
            count=5
        )

        if result["success"]:
            articles = result["data"]["articles"]
            return self.format_response(articles)
        else:
            return f"Failed to get news: {result['error']}"

    def extract_query(self, message: str) -> str:
        """Extract search query from message."""
        # Simple implementation - enhance as needed
        stop_words = ["get", "find", "search", "news", "about", "on", "for"]
        words = message.lower().split()
        filtered_words = [w for w in words if w not in stop_words]
        return " ".join(filtered_words)

    def format_response(self, articles: list) -> str:
        """Format articles for response."""
        if not articles:
            return "No relevant news articles found."

        response = f"Here are {len(articles)} relevant news articles:\\n\\n"

        for i, article in enumerate(articles, 1):
            response += f"{i}. **{article['title']}**\\n"
            response += f"   *Source: {article['source']}*\\n"
            if article.get('summary'):
                response += f"   {article['summary']}\\n"
            response += f"   [Read more]({article['url']})\\n\\n"

        return response
'''

    async def health_check(self) -> Dict[str, Any]:
        """Perform health check."""
        health = await super().health_check()
        health["autogpt_available"] = getattr(self, '_autogpt_available', False)

        if hasattr(self, '_autogpt_available') and self._autogpt_available:
            try:
                import autogpt
                health["autogpt_version"] = getattr(autogpt, '__version__', 'unknown')
            except:
                health["autogpt_version"] = "unknown"

        return health