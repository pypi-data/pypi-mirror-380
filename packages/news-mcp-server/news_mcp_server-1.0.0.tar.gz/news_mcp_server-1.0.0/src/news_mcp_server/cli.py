"""Command line interface for News MCP Server."""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Optional

import click
import uvicorn

from .core.config import load_config, Config
from .core.server import create_app


def setup_logging(log_level: str = "INFO") -> None:
    """Setup logging configuration."""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )


@click.group()
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True, path_type=Path),
    help="Path to configuration file"
)
@click.option(
    "--log-level",
    default="INFO",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"], case_sensitive=False),
    help="Logging level"
)
@click.pass_context
def cli(ctx: click.Context, config: Optional[Path], log_level: str) -> None:
    """News MCP Server - Hybrid MCP server for news aggregation."""
    ctx.ensure_object(dict)
    ctx.obj["config_path"] = str(config) if config else None
    ctx.obj["log_level"] = log_level
    setup_logging(log_level)


@cli.command()
@click.option(
    "--host",
    default="0.0.0.0",
    help="Host to bind the server to"
)
@click.option(
    "--port",
    default=3000,
    type=int,
    help="Port to bind the server to"
)
@click.option(
    "--reload",
    is_flag=True,
    help="Enable auto-reload for development"
)
@click.option(
    "--workers",
    default=1,
    type=int,
    help="Number of worker processes"
)
@click.pass_context
def run(ctx: click.Context, host: str, port: int, reload: bool, workers: int) -> None:
    """Run the News MCP Server."""
    config_path = ctx.obj.get("config_path")

    try:
        # Load configuration
        config = load_config(config_path)

        # Validate configuration
        issues = config.validate_config()
        if issues:
            click.echo("Configuration issues found:", err=True)
            for issue in issues:
                click.echo(f"  - {issue}", err=True)
            sys.exit(1)

        # Override with CLI parameters
        if host != "0.0.0.0":
            config.server.host = host
        if port != 3000:
            config.server.port = port
        if reload:
            config.server.reload = reload

        click.echo(f"Starting News MCP Server on {config.server.host}:{config.server.port}")
        click.echo(f"Configuration: {config_path or 'environment/defaults'}")

        # Create and run the application
        uvicorn.run(
            "news_mcp_server.core.server:create_app",
            host=config.server.host,
            port=config.server.port,
            reload=config.server.reload,
            workers=workers if not reload else 1,
            log_level=config.server.log_level.lower(),
            factory=True
        )

    except Exception as e:
        click.echo(f"Error starting server: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.pass_context
def validate(ctx: click.Context) -> None:
    """Validate configuration."""
    config_path = ctx.obj.get("config_path")

    try:
        config = load_config(config_path)
        issues = config.validate_config()

        if issues:
            click.echo("Configuration validation failed:", err=True)
            for issue in issues:
                click.echo(f"  - {issue}", err=True)
            sys.exit(1)
        else:
            click.echo("Configuration is valid ✓")

    except Exception as e:
        click.echo(f"Error validating configuration: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.pass_context
def config_info(ctx: click.Context) -> None:
    """Show current configuration."""
    config_path = ctx.obj.get("config_path")

    try:
        config = load_config(config_path)

        click.echo("News MCP Server Configuration:")
        click.echo(f"  Config file: {config_path or 'environment/defaults'}")
        click.echo(f"  Server: {config.server.host}:{config.server.port}")
        click.echo(f"  Cache: {'enabled' if config.cache.enabled else 'disabled'}")
        if config.cache.enabled:
            click.echo(f"    Provider: {config.cache.provider}")
            click.echo(f"    TTL: {config.cache.ttl}s")
        click.echo(f"  Monitoring: {'enabled' if config.monitoring.enabled else 'disabled'}")
        click.echo(f"  Press Monitor API: {'configured' if config.get_press_monitor_auth() else 'not configured'}")

        # Show news APIs
        if config.news_apis:
            click.echo("  News APIs:")
            for name, api_config in config.news_apis.items():
                click.echo(f"    {name}: {api_config.base_url}")

    except Exception as e:
        click.echo(f"Error loading configuration: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option(
    "--url",
    default="http://localhost:3000",
    help="Server URL to check"
)
def health(url: str) -> None:
    """Check server health status."""
    import httpx

    async def check_health():
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{url}/health", timeout=10.0)
                response.raise_for_status()
                health_data = response.json()

                status = health_data.get("status", "unknown")
                click.echo(f"Server status: {status}")

                if "services" in health_data:
                    click.echo("Services:")
                    for service, info in health_data["services"].items():
                        service_status = info.get("status", "unknown")
                        click.echo(f"  {service}: {service_status}")

                return status == "healthy"

        except Exception as e:
            click.echo(f"Health check failed: {e}", err=True)
            return False

    is_healthy = asyncio.run(check_health())
    sys.exit(0 if is_healthy else 1)


@cli.command()
@click.option(
    "--url",
    default="http://localhost:3000",
    help="Server URL"
)
@click.option(
    "--query",
    required=True,
    help="Search query"
)
@click.option(
    "--country",
    help="Country code (e.g., US)"
)
@click.option(
    "--lang",
    help="Language code (e.g., en)"
)
@click.option(
    "--count",
    default=5,
    type=int,
    help="Number of results"
)
def test(url: str, query: str, country: Optional[str], lang: Optional[str], count: int) -> None:
    """Test the server with a sample query."""
    import httpx
    import json

    async def test_query():
        try:
            async with httpx.AsyncClient() as client:
                # Prepare MCP request
                mcp_request = {
                    "jsonrpc": "2.0",
                    "id": "1",
                    "method": "news_headlines",
                    "params": {
                        "query_text": query,
                        "count": count
                    }
                }

                if country:
                    mcp_request["params"]["country_code"] = country
                if lang:
                    mcp_request["params"]["lang_code"] = lang

                # Make request
                response = await client.post(
                    f"{url}/mcp",
                    json=mcp_request,
                    timeout=30.0
                )
                response.raise_for_status()
                result = response.json()

                click.echo("Test request successful!")
                click.echo(f"Query: {query}")

                if "result" in result:
                    items = result["result"].get("items", [])
                    click.echo(f"Found {len(items)} articles:")

                    for i, item in enumerate(items[:3], 1):
                        title = item.get("title", "No title")
                        source = item.get("source", "Unknown source")
                        click.echo(f"  {i}. {title} ({source})")

                    if result["result"].get("cached"):
                        click.echo("  (served from cache)")

                elif "error" in result:
                    error = result["error"]
                    click.echo(f"Error: {error.get('message', 'Unknown error')}")

        except Exception as e:
            click.echo(f"Test failed: {e}", err=True)
            sys.exit(1)

    asyncio.run(test_query())


def main() -> None:
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()