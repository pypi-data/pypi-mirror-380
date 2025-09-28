"""Vercel serverless handler for News MCP Server."""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.server import NewsMCPServer
from .core.config import Config


# Create a lightweight config for serverless
def create_serverless_config() -> Config:
    """Create configuration optimized for serverless deployment."""
    config = Config()

    # Override for serverless environment
    config.cache.enabled = bool(os.getenv("REDIS_URL"))
    config.cache.provider = "memory" if not config.cache.enabled else "redis"
    config.monitoring.enabled = False  # Disable heavy monitoring in serverless

    # Use environment variables
    if redis_url := os.getenv("REDIS_URL"):
        config.cache.redis_url = redis_url

    return config


# Create FastAPI app for Vercel
config = create_serverless_config()
server = NewsMCPServer(config)
app = server.app

# Add CORS for web usage
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Vercel handler
def handler(request, context):
    """Vercel serverless handler."""
    return app(request, context)