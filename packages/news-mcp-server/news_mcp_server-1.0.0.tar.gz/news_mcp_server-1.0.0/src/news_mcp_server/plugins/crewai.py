"""CrewAI integration plugin for News MCP Server."""

import logging
from typing import Any, Dict, List, Optional

from .base import FrameworkPlugin, PluginMetadata, PluginType, PluginConfig


logger = logging.getLogger(__name__)


class CrewAIPlugin(FrameworkPlugin):
    """CrewAI framework integration plugin."""

    def __init__(self, config: Optional[PluginConfig] = None):
        super().__init__(config)

    @property
    def metadata(self) -> PluginMetadata:
        """Get plugin metadata."""
        return PluginMetadata(
            name="crewai-integration",
            version="1.0.0",
            description="CrewAI framework integration for News MCP Server",
            author="News MCP Team",
            plugin_type=PluginType.FRAMEWORK_INTEGRATION,
            dependencies=["crewai", "crewai-tools"],
            supported_formats=["tool", "agent"]
        )

    async def initialize(self) -> bool:
        """Initialize CrewAI plugin."""
        try:
            # Check if CrewAI is available
            try:
                import crewai
                logger.info(f"CrewAI {crewai.__version__} detected")
            except ImportError:
                logger.warning("CrewAI not installed. Plugin will provide installation instructions.")
                self._crewai_available = False
            else:
                self._crewai_available = True

            self._initialized = True
            logger.info("CrewAI plugin initialized successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to initialize CrewAI plugin: {e}")
            return False

    async def shutdown(self) -> None:
        """Shutdown CrewAI plugin."""
        logger.info("CrewAI plugin shutting down")

    async def create_tool(self, server_url: str, api_key: Optional[str] = None) -> Any:
        """Create CrewAI tool for News MCP Server."""
        if not self._crewai_available:
            raise ImportError("CrewAI is not installed. Install with: pip install crewai crewai-tools")

        from crewai_tools import BaseTool
        from pydantic import Field
        import httpx
        import json

        class NewsMCPTool(BaseTool):
            """CrewAI tool for News MCP Server."""

            name: str = "news_search_tool"
            description: str = """
            Search for news articles using the News MCP Server.
            Useful for finding current news, breaking stories, and specific topics.

            Args:
                query (str): Search terms for news articles
                news_type (str): Type of news data - 'headlines', 'briefs', 'fulltext', or 'metadata'
                country_code (str, optional): Country codes like 'US', 'CA', 'UK'
                lang_code (str, optional): Language codes like 'en', 'es', 'fr'
                count (int, optional): Number of articles to return (default: 10, max: 100)
            """

            server_url: str = Field(description="MCP Server URL")
            api_key: Optional[str] = Field(default=None, description="API Key")

            def _run(
                self,
                query: str,
                news_type: str = "briefs",
                country_code: Optional[str] = None,
                lang_code: Optional[str] = None,
                count: int = 10
            ) -> str:
                """Execute the news search tool."""
                try:
                    # Validate news type
                    valid_types = ["headlines", "briefs", "fulltext", "metadata"]
                    if news_type not in valid_types:
                        return f"Error: news_type must be one of {valid_types}"

                    # Prepare MCP request
                    mcp_method = f"news_{news_type}"
                    mcp_params = {
                        "query_text": query,
                        "count": min(count, 100)  # Cap at 100
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

                        # Format response for CrewAI
                        news_data = result.get("result", {})
                        items = news_data.get("items", [])
                        credits = news_data.get("credits", {})

                        if not items:
                            return f"No news articles found for query: '{query}'"

                        # Create detailed response
                        response_text = f"Found {len(items)} news articles for '{query}':\\n\\n"

                        for i, item in enumerate(items, 1):
                            response_text += f"Article {i}:\\n"
                            response_text += f"Title: {item.get('title', 'No title')}\\n"
                            response_text += f"Source: {item.get('source', 'Unknown')}\\n"
                            response_text += f"URL: {item.get('url', 'No URL')}\\n"

                            if 'description' in item:
                                response_text += f"Summary: {item['description']}\\n"

                            if 'body' in item and news_type == 'fulltext':
                                body = item['body'][:500]  # Truncate for readability
                                response_text += f"Content: {body}{'...' if len(item['body']) > 500 else ''}\\n"

                            if 'entities' in item and news_type == 'metadata':
                                entities = [e.get('name', '') for e in item.get('entities', [])[:5]]
                                if entities:
                                    response_text += f"Key Entities: {', '.join(entities)}\\n"

                            response_text += "\\n"

                        # Add metadata
                        if credits:
                            response_text += f"\\nCredits used: {credits.get('quantity', 0)}\\n"

                        return response_text

                except Exception as e:
                    return f"Error executing news search: {str(e)}"

        return NewsMCPTool(server_url=server_url, api_key=api_key)

    def get_example_usage(self) -> str:
        """Get example usage code."""
        return '''
# CrewAI Integration Example

from crewai import Agent, Task, Crew, LLM
from news_mcp_server.plugins import CrewAIPlugin

# Initialize plugin
plugin = CrewAIPlugin()
await plugin.initialize()

# Create news search tool
news_tool = await plugin.create_tool(
    server_url="http://localhost:3000",
    api_key="your-api-key"
)

# Create an LLM instance
llm = LLM(model="gpt-4o-mini")

# Create a news research agent
news_researcher = Agent(
    role="News Researcher",
    goal="Find and analyze relevant news articles on given topics",
    backstory="""You are an expert news researcher who can quickly find and
                 summarize the most important news stories on any topic.""",
    tools=[news_tool],
    llm=llm,
    verbose=True
)

# Create a news analyst agent
news_analyst = Agent(
    role="News Analyst",
    goal="Analyze news trends and provide insights",
    backstory="""You are a seasoned news analyst who can identify patterns,
                 trends, and important implications from news stories.""",
    llm=llm,
    verbose=True
)

# Define tasks
research_task = Task(
    description="""Research the latest news about artificial intelligence and
                   machine learning breakthroughs. Focus on recent developments
                   in the last week.""",
    agent=news_researcher,
    expected_output="A comprehensive summary of recent AI/ML news with key points"
)

analysis_task = Task(
    description="""Analyze the news findings and identify the most significant
                   trends and their potential impact on the technology industry.""",
    agent=news_analyst,
    expected_output="An analytical report on AI/ML trends and industry impact",
    context=[research_task]
)

# Create and run crew
crew = Crew(
    agents=[news_researcher, news_analyst],
    tasks=[research_task, analysis_task],
    verbose=True
)

result = crew.kickoff()
print(result)

# Direct tool usage
direct_result = news_tool._run(
    query="quantum computing breakthrough",
    news_type="fulltext",
    country_code="US",
    count=5
)
print(direct_result)
'''

    def create_agent_template(self, server_url: str, api_key: Optional[str] = None) -> str:
        """Create a template for a news-focused CrewAI agent."""
        return f'''
# News Research Agent Template for CrewAI

from crewai import Agent, LLM
from news_mcp_server.plugins import CrewAIPlugin

# Initialize and get tool
plugin = CrewAIPlugin()
await plugin.initialize()
news_tool = await plugin.create_tool("{server_url}", "{api_key or 'your-api-key'}")

# LLM configuration
llm = LLM(model="gpt-4o-mini")

# News Research Agent
news_agent = Agent(
    role="News Research Specialist",
    goal="Find, analyze, and summarize news articles on specific topics",
    backstory="""You are an experienced news researcher with expertise in finding
                 relevant, timely, and credible news sources. You excel at
                 summarizing complex news stories and identifying key trends.""",
    tools=[news_tool],
    llm=llm,
    max_iter=3,
    memory=True,
    verbose=True,
    allow_delegation=False
)

# Example specialized agents for different news categories
tech_news_agent = Agent(
    role="Technology News Analyst",
    goal="Specialize in technology and innovation news coverage",
    backstory="""You are a technology journalist with deep understanding of
                 tech trends, startups, and innovation. You can quickly identify
                 important technological developments and their implications.""",
    tools=[news_tool],
    llm=llm
)

business_news_agent = Agent(
    role="Business News Analyst",
    goal="Focus on business, finance, and economic news",
    backstory="""You are a business journalist with expertise in financial
                 markets, corporate news, and economic trends. You understand
                 the business implications of news events.""",
    tools=[news_tool],
    llm=llm
)

# Usage examples:
# tech_news_agent can research: "AI startups", "tech IPOs", "semiconductor industry"
# business_news_agent can research: "stock market", "merger acquisitions", "economic indicators"
'''

    async def health_check(self) -> Dict[str, Any]:
        """Perform health check."""
        health = await super().health_check()
        health["crewai_available"] = getattr(self, '_crewai_available', False)

        if hasattr(self, '_crewai_available') and self._crewai_available:
            try:
                import crewai
                health["crewai_version"] = crewai.__version__
            except:
                health["crewai_version"] = "unknown"

        return health