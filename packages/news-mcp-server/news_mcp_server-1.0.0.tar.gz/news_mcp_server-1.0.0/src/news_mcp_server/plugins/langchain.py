"""LangChain integration plugin for News MCP Server."""

import logging
from typing import Any, Dict, List, Optional

from .base import FrameworkPlugin, PluginMetadata, PluginType, PluginConfig


logger = logging.getLogger(__name__)


class LangChainPlugin(FrameworkPlugin):
    """LangChain framework integration plugin."""

    def __init__(self, config: Optional[PluginConfig] = None):
        super().__init__(config)

    @property
    def metadata(self) -> PluginMetadata:
        """Get plugin metadata."""
        return PluginMetadata(
            name="langchain-integration",
            version="1.0.0",
            description="LangChain framework integration for News MCP Server",
            author="News MCP Team",
            plugin_type=PluginType.FRAMEWORK_INTEGRATION,
            dependencies=["langchain", "langchain-community"],
            supported_formats=["tool", "retriever", "loader"]
        )

    async def initialize(self) -> bool:
        """Initialize LangChain plugin."""
        try:
            # Check if LangChain is available
            try:
                import langchain
                logger.info(f"LangChain {langchain.__version__} detected")
            except ImportError:
                logger.warning("LangChain not installed. Plugin will provide installation instructions.")
                self._langchain_available = False
            else:
                self._langchain_available = True

            self._initialized = True
            logger.info("LangChain plugin initialized successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to initialize LangChain plugin: {e}")
            return False

    async def shutdown(self) -> None:
        """Shutdown LangChain plugin."""
        logger.info("LangChain plugin shutting down")

    async def create_tool(self, server_url: str, api_key: Optional[str] = None) -> Any:
        """Create LangChain tool for News MCP Server."""
        if not self._langchain_available:
            raise ImportError("LangChain is not installed. Install with: pip install langchain langchain-community")

        from langchain.tools import BaseTool
        from langchain.callbacks.manager import CallbackManagerForToolRun
        from pydantic import Field
        import httpx
        import json

        class NewsMCPTool(BaseTool):
            """LangChain tool for News MCP Server."""

            name: str = "news_search"
            description: str = """
            Search for news articles using the News MCP Server.
            Input should be a JSON string with query parameters:
            {
                "query": "search terms",
                "type": "headlines|briefs|fulltext|metadata",
                "country_code": "US,CA (optional)",
                "lang_code": "en (optional)",
                "count": 10
            }
            """

            server_url: str = Field(description="MCP Server URL")
            api_key: Optional[str] = Field(default=None, description="API Key")

            def _run(
                self,
                query: str,
                run_manager: Optional[CallbackManagerForToolRun] = None,
            ) -> str:
                """Execute the tool."""
                try:
                    # Parse input
                    params = json.loads(query)
                    query_text = params.get("query", "")
                    news_type = params.get("type", "headlines")
                    country_code = params.get("country_code")
                    lang_code = params.get("lang_code")
                    count = params.get("count", 10)

                    # Prepare MCP request
                    mcp_method = f"news_{news_type}"
                    mcp_params = {
                        "query_text": query_text,
                        "count": count
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

                    with httpx.Client() as client:
                        response = client.post(
                            f"{self.server_url}/mcp",
                            json=mcp_request,
                            headers=headers,
                            timeout=30.0
                        )
                        response.raise_for_status()

                        result = response.json()
                        if result.get("error"):
                            return f"Error: {result['error']['message']}"

                        # Format response for LangChain
                        news_data = result.get("result", {})
                        items = news_data.get("items", [])

                        if not items:
                            return "No news articles found for the given query."

                        # Create summary
                        summary = f"Found {len(items)} news articles:\n\n"
                        for i, item in enumerate(items[:5], 1):  # Limit to first 5
                            summary += f"{i}. {item.get('title', 'No title')}\n"
                            summary += f"   Source: {item.get('source', 'Unknown')}\n"
                            summary += f"   URL: {item.get('url', 'No URL')}\n"

                            if 'description' in item:
                                summary += f"   Summary: {item['description'][:200]}...\n"

                            summary += "\n"

                        return summary

                except json.JSONDecodeError:
                    return "Error: Invalid JSON input. Please provide valid JSON with query parameters."
                except Exception as e:
                    return f"Error executing news search: {str(e)}"

            async def _arun(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
                """Async version of the tool."""
                # For now, delegate to sync version
                return self._run(query, run_manager)

        return NewsMCPTool(server_url=server_url, api_key=api_key)

    def get_example_usage(self) -> str:
        """Get example usage code."""
        return '''
# LangChain Integration Example

from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from news_mcp_server.plugins import LangChainPlugin

# Initialize plugin
plugin = LangChainPlugin()
await plugin.initialize()

# Create tool
news_tool = await plugin.create_tool(
    server_url="http://localhost:3000",
    api_key="your-api-key"
)

# Use with LangChain agent
llm = OpenAI(temperature=0)
tools = [news_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example usage
result = agent.run("""
Find recent news about artificial intelligence and summarize the key developments.
""")

print(result)

# Direct tool usage
news_result = news_tool.run(\'\'\'
{
    "query": "artificial intelligence",
    "type": "briefs",
    "country_code": "US",
    "count": 5
}
\'\'\')

print(news_result)
'''

    def create_retriever(self, server_url: str, api_key: Optional[str] = None) -> Any:
        """Create LangChain retriever for News MCP Server."""
        if not self._langchain_available:
            raise ImportError("LangChain is not installed")

        from langchain.schema import BaseRetriever, Document
        from pydantic import Field
        import httpx
        from typing import List

        class NewsMCPRetriever(BaseRetriever):
            """LangChain retriever for News MCP Server."""

            server_url: str = Field(description="MCP Server URL")
            api_key: Optional[str] = Field(default=None, description="API Key")
            default_count: int = Field(default=10, description="Default number of results")
            default_type: str = Field(default="briefs", description="Default news type")

            def _get_relevant_documents(self, query: str) -> List[Document]:
                """Get relevant documents."""
                try:
                    # Prepare MCP request
                    mcp_request = {
                        "jsonrpc": "2.0",
                        "id": "1",
                        "method": f"news_{self.default_type}",
                        "params": {
                            "query_text": query,
                            "count": self.default_count
                        }
                    }

                    # Make request
                    headers = {"Content-Type": "application/json"}
                    if self.api_key:
                        headers["X-API-Key"] = self.api_key

                    with httpx.Client() as client:
                        response = client.post(
                            f"{self.server_url}/mcp",
                            json=mcp_request,
                            headers=headers,
                            timeout=30.0
                        )
                        response.raise_for_status()

                        result = response.json()
                        if result.get("error"):
                            return []

                        # Convert to LangChain documents
                        documents = []
                        items = result.get("result", {}).get("items", [])

                        for item in items:
                            content = item.get("title", "")
                            if item.get("description"):
                                content += f"\\n\\n{item['description']}"
                            if item.get("body"):
                                content += f"\\n\\n{item['body']}"

                            metadata = {
                                "source": item.get("source", ""),
                                "url": item.get("url", ""),
                                "country_code": item.get("country_code", ""),
                                "lang_code": item.get("lang_code", ""),
                                "timestamp": item.get("ts", 0)
                            }

                            documents.append(Document(
                                page_content=content,
                                metadata=metadata
                            ))

                        return documents

                except Exception as e:
                    logger.error(f"Error in NewsMCPRetriever: {e}")
                    return []

            async def _aget_relevant_documents(self, query: str) -> List[Document]:
                """Async version of get_relevant_documents."""
                return self._get_relevant_documents(query)

        return NewsMCPRetriever(server_url=server_url, api_key=api_key)

    async def health_check(self) -> Dict[str, Any]:
        """Perform health check."""
        health = await super().health_check()
        health["langchain_available"] = getattr(self, '_langchain_available', False)

        if hasattr(self, '_langchain_available') and self._langchain_available:
            try:
                import langchain
                health["langchain_version"] = langchain.__version__
            except:
                health["langchain_version"] = "unknown"

        return health