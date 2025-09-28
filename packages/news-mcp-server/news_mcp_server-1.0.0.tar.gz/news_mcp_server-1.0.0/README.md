# Global News MCP Server - 200 Countries, 100+ Languages. Millions of News Items Everyday!

[![PyPI version](https://badge.fury.io/py/news-mcp-server.svg)](https://badge.fury.io/py/news-mcp-server)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/news-mcp-server)](https://pepy.tech/project/news-mcp-server)

## 🌍 Real-Time Global News Intelligence for AI Agents & Applications

**News MCP Server** is a production-ready **Model Context Protocol (MCP) server** that provides **real-time, multilingual news intelligence** from **200+ countries** and **18+ languages**. Built for **AI agents, autonomous applications, and enterprise workflows**, it delivers structured news data with **advanced filtering, caching, and framework integrations**.

Perfect for **LLM applications, AI agents, research platforms, compliance monitoring, brand reputation tracking, and market intelligence**.

---

## 🚀 Quick Start

### Installation

```bash
# Core installation
pip install news-mcp-server

# Full installation with Redis caching & monitoring
pip install news-mcp-server[full]

# AI framework integrations (LangChain, CrewAI)
pip install news-mcp-server[frameworks]

# Enterprise cloud features
pip install news-mcp-server[cloud]

# Everything included
pip install news-mcp-server[all]
```

### Basic Usage

```bash
# Start the MCP server
news-mcp-server run

# Server runs on http://localhost:3000
# Health check: http://localhost:3000/health
# Metrics: http://localhost:3000/metrics
```

### Environment Setup

```bash
# Required: Press Monitor API credentials
# Get your API key: https://aws.amazon.com/marketplace/pp/prodview-vpx4cz3ekl3b2?sr=0-2&ref_=beagle&applicationId=AWSMPContessa
export PRESS_MONITOR_API_KEY="your_secret_key:subscription_id"

# Optional: Server authentication
export NEWS_MCP_API_KEY="your_server_api_key"

# Optional: Redis for enterprise caching
export REDIS_URL="redis://localhost:6379/0"
```

---

## 🎯 Key Features

### 🌐 **Global News Coverage**
- **200+ countries** with real-time monitoring
- **18+ languages** including English, Spanish, French, Arabic, Chinese, Hindi
- **Thousands of sources**: newspapers, news websites, blogs, select social channels

### 🤖 **AI-Ready Integration**
- **MCP (Model Context Protocol)** for seamless AI agent integration
- **Structured JSON responses** optimized for LLM consumption
- **Built-in LangChain, CrewAI, AutoGPT** integrations
- **OpenAI, Claude, GPT-4** compatible

### 📊 **Rich Data & Metadata**
- **Headlines, briefs, full-text articles**
- **Images, entities, sentiment analysis**
- **Wikidata-aligned metadata** for advanced analytics
- **Geographic and temporal filtering**

### ⚡ **Production-Ready**
- **High-performance Redis caching**
- **Prometheus metrics & health checks**
- **Rate limiting & circuit breakers**
- **Docker & Kubernetes ready**

---

## 📖 API Endpoints

### Core MCP Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| `news_headlines` | Get news headlines with titles, URLs, sources | Quick news updates, notifications |
| `news_briefs` | Get news summaries with descriptions | Content feeds, dashboards |
| `news_fulltext` | Get complete articles with full content | Research, analysis, archiving |
| `news_fulltext_metadata` | Get articles with entities, Wikidata IDs | Advanced analytics, compliance |
| `news_headlines_translated` | Get translated headlines | Multilingual applications |

### Example MCP Request

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "news_headlines",
  "params": {
    "query_text": "artificial intelligence breakthrough",
    "country_code": "US",
    "lang_code": "en",
    "count": 10,
    "sort": "latest"
  }
}
```

### Python SDK Usage

```python
from news_mcp_server.api.client import NewsMCPClient

async with NewsMCPClient(
    server_url="http://localhost:3000",
    api_key="your_api_key"
) as client:

    # Get AI news headlines
    headlines = await client.get_headlines(
        query="machine learning",
        country_code="US",
        count=5
    )

    for article in headlines.items:
        print(f"📰 {article.title}")
        print(f"🏢 {article.source}")
        print(f"🔗 {article.url}\n")
```

---

## 🤖 AI Framework Integrations

### LangChain Integration

```python
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from news_mcp_server.plugins.langchain import LangChainPlugin

# Initialize news tool
plugin = LangChainPlugin()
await plugin.initialize()

news_tool = await plugin.create_tool(
    server_url="http://localhost:3000",
    api_key="your_api_key"
)

# Create AI agent with news capabilities
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[news_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Ask agent to find and analyze news
result = agent.run("""
Find recent news about AI breakthroughs in healthcare
and provide a summary of key developments
""")
```

### CrewAI Integration

```python
from crewai import Agent, Task, Crew
from news_mcp_server.plugins.crewai import CrewAIPlugin

# Create news-powered AI agent
news_agent = Agent(
    role='News Analyst',
    goal='Find and analyze relevant news for insights',
    backstory='Expert at finding and interpreting news trends',
    tools=[news_tool]
)

# Define analysis task
analysis_task = Task(
    description="Find news about renewable energy investments and analyze trends",
    agent=news_agent
)

# Execute with crew
crew = Crew(agents=[news_agent], tasks=[analysis_task])
result = crew.kickoff()
```

---

## 🔧 Installation Variants

### Minimal Installation
```bash
pip install news-mcp-server
# Core MCP server only (~20MB)
```

### Production Installation
```bash
pip install news-mcp-server[full]
# Includes Redis caching, monitoring, health checks
```

### AI Development
```bash
pip install news-mcp-server[frameworks]
# Includes LangChain, CrewAI integrations
```

### Enterprise Cloud
```bash
pip install news-mcp-server[cloud]
# Includes AWS, Azure, GCP integrations
```

---

## 🚀 Deployment Options

### Local Development
```bash
# Start with auto-reload
news-mcp-server run --reload

# With debug logging
news-mcp-server run --log-level debug
```

### Docker Deployment
```bash
# Pull and run
docker run -p 3000:3000 \
  -e PRESS_MONITOR_API_KEY=your_key \
  news-mcp-server:latest
```

### Production Configuration
```bash
# With Redis and monitoring
news-mcp-server run \
  --config production.json \
  --workers 4
```

---

## 🎯 Use Cases

### 🤖 **AI Agent Applications**
- **Autonomous research agents** with real-time news access
- **Content generation** with current events context
- **Market analysis bots** for trading and investment
- **Compliance monitoring** for regulatory changes

### 📊 **Enterprise Intelligence**
- **Brand reputation monitoring** across global media
- **Competitive intelligence** and market trends
- **Risk assessment** and geopolitical analysis
- **Executive briefings** with AI-powered summaries

### 🔬 **Research & Analytics**
- **Academic research** with structured news data
- **Sentiment analysis** on global events
- **Social listening** and trend analysis
- **Policy impact assessment**

### 🏢 **Business Applications**
- **CRM integration** with relevant industry news
- **Marketing intelligence** and campaign optimization
- **Sales enablement** with prospect context
- **Customer success** with account-relevant updates

---

## 🔍 Search & Filtering

### Geographic Filtering
```python
# US technology news
headlines = await client.get_headlines(
    query="technology innovation",
    country_code="US"
)

# European markets
headlines = await client.get_headlines(
    query="financial markets",
    country_code="DE,FR,IT"
)
```

### Language Support
```python
# Spanish language news
headlines = await client.get_headlines(
    query="inteligencia artificial",
    lang_code="es"
)

# Multilingual search
headlines = await client.get_headlines(
    query="climate change",
    lang_code="en,fr,de"
)
```

### Advanced Queries
```python
# Time-sensitive searches
headlines = await client.get_headlines(
    query="earnings report",
    sort="latest",
    count=50
)

# Relevance-based ranking
headlines = await client.get_headlines(
    query="artificial intelligence breakthrough",
    sort="relevance",
    count=20
)
```

---

## 📈 Performance & Monitoring

### Built-in Monitoring
- **Prometheus metrics** at `/metrics`
- **Health checks** at `/health`
- **Request/response tracking**
- **Cache hit rate monitoring**

### Caching Strategy
- **Redis integration** for enterprise performance
- **Memory fallback** for development
- **Configurable TTL** (default: 5 minutes)
- **Automatic cache invalidation**

### Rate Limiting
- **Configurable limits** (default: 60/minute)
- **Burst protection** (100 requests/30s)
- **Client-specific quotas**
- **Graceful degradation**

---

## 🛠️ Configuration

### Configuration File (`config.json`)
```json
{
  "server": {
    "host": "0.0.0.0",
    "port": 3000,
    "log_level": "info"
  },
  "cache": {
    "provider": "redis",
    "redis_url": "redis://localhost:6379/0",
    "ttl": 300,
    "enabled": true
  },
  "monitoring": {
    "enabled": true,
    "metrics_endpoint": "/metrics",
    "health_endpoint": "/health"
  },
  "security": {
    "rate_limiting": {
      "enabled": true,
      "requests_per_minute": 60
    }
  }
}
```

### Environment Variables
```bash
# Core configuration
PRESS_MONITOR_API_KEY=your_secret_key:subscription_id
NEWS_MCP_API_KEY=your_server_api_key

# Performance tuning
REDIS_URL=redis://localhost:6379/0
CACHE_TTL=300
MAX_WORKERS=4

# Security
RATE_LIMIT_ENABLED=true
REQUESTS_PER_MINUTE=60
```

---

## 🔐 Security Features

- **API key authentication** for server access
- **Bearer token validation** for Press Monitor API
- **Rate limiting** to prevent abuse
- **Input validation** and sanitization
- **CORS configuration** for web applications
- **Request logging** for audit trails

---

## 📚 Documentation & Support

### Resources
- **[API Documentation](https://www.pressmonitor.com/en/docs/online-news-api)** - Comprehensive API reference
- **[Open API Schema](https://api.pressmonitor.com/schemas/newsv1)** - API schema specification
- **[Press Monitor Website](https://www.pressmonitor.com/)** - Official vendor website
- **[GitHub Repository](https://github.com/press-monitor/global-news-mcp-server)** - Source code and issues
- **[Examples Collection](https://github.com/press-monitor/global-news-mcp-server/tree/main/examples)** - Integration examples

### Community Support
- **GitHub Issues** - Bug reports and feature requests
- **Discord Server** - Real-time community help
- **Stack Overflow** - Tag: `news-mcp-server`
- **Email Support** - support@pressmonitor.com (1-2 working days response time)

---

## 🏗️ Advanced Features

### Custom Plugins
```python
from news_mcp_server.plugins.base import FrameworkPlugin

class CustomNewsPlugin(FrameworkPlugin):
    async def create_tool(self, server_url, api_key):
        # Custom integration logic
        pass
```

### Webhook Integration
```python
# Real-time news alerts
await client.setup_webhook(
    url="https://yourapp.com/news-webhook",
    events=["new_article", "trending_topic"],
    filters={"query": "your_keywords"}
)
```

### Batch Processing
```python
# Process multiple queries efficiently
queries = [
    {"query_text": "AI", "country_code": "US"},
    {"query_text": "blockchain", "country_code": "UK"},
    {"query_text": "sustainability", "country_code": "DE"}
]

results = await client.batch_search(queries)
```

---

## 🏆 Why Choose News MCP Server?

### ✅ **Production Ready**
- Battle-tested in enterprise environments
- 99.9% uptime SLA available
- Comprehensive monitoring and alerting
- Horizontal scaling support

### ✅ **Developer Friendly**
- One-line installation with pip
- Extensive documentation and examples
- Active community and support
- Framework-agnostic design

### ✅ **AI Optimized**
- Purpose-built for LLM applications
- Structured data perfect for AI consumption
- Built-in framework integrations
- Optimized for agent workflows

### ✅ **Global Scale**
- 200+ countries covered
- 18+ languages supported
- Real-time data processing
- Enterprise-grade infrastructure

---

## 📊 Pricing & Usage

### Free Tier
- Up to 1,000 requests/month
- Basic news headlines and briefs
- Community support
- Perfect for development and testing

### Professional Tier ($49/month)
- Up to 50,000 requests/month
- Full-text articles and metadata
- Redis caching included
- Email support

### Enterprise Tier (Custom)
- Unlimited requests
- SLA and dedicated support
- Custom integrations
- On-premise deployment options

---

## 🚀 Get Started Today

```bash
# Install the package
pip install news-mcp-server[full]

# Get your API key from Press Monitor
# https://aws.amazon.com/marketplace/pp/prodview-vpx4cz3ekl3b2?sr=0-2&ref_=beagle&applicationId=AWSMPContessa

# Set up environment
export PRESS_MONITOR_API_KEY="your_key"

# Start the server
news-mcp-server run

# Test with a simple request
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "news_headlines",
    "params": {
      "query_text": "artificial intelligence",
      "count": 5
    }
  }'
```

**Transform your AI applications with real-time global news intelligence. Start building today!** 🚀

---

**Keywords**: news API, MCP server, AI agent integration, global news search, real-time media monitoring, LangChain news tool, CrewAI integration, multilingual news API, enterprise news intelligence, Python news API, AI-powered media monitoring, autonomous agent tools
