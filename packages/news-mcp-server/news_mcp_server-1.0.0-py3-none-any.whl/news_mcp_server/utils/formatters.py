"""Response and data formatting utilities."""

import hashlib
import json
from typing import Any, Dict, Optional
from datetime import datetime


def format_news_response(
    data: Dict[str, Any],
    cached: bool = False,
    processing_time: Optional[float] = None
) -> Dict[str, Any]:
    """
    Format news response with metadata.

    Args:
        data: Raw news data from API
        cached: Whether response was served from cache
        processing_time: Processing time in seconds

    Returns:
        Formatted response with metadata
    """
    formatted = data.copy()

    # Add metadata
    formatted["cached"] = cached

    if processing_time is not None:
        formatted["processing_time"] = processing_time

    # Add cache TTL if cached
    if cached:
        formatted["cache_ttl"] = 300  # Default TTL

    # Format timestamps for readability
    if "items" in formatted:
        for item in formatted["items"]:
            if "ts" in item:
                try:
                    item["published_at"] = datetime.fromtimestamp(item["ts"]).isoformat()
                except (ValueError, OSError):
                    pass

    return formatted


def format_cache_key(
    endpoint: str,
    params: Dict[str, Any],
    max_length: int = 200
) -> str:
    """
    Create a consistent cache key from endpoint and parameters.

    Args:
        endpoint: API endpoint name
        params: Query parameters
        max_length: Maximum key length before hashing

    Returns:
        Cache key string
    """
    # Remove None values and sort for consistency
    clean_params = {k: v for k, v in params.items() if v is not None}
    sorted_params = sorted(clean_params.items())

    # Create base key
    param_str = "&".join(f"{k}={v}" for k, v in sorted_params)
    key = f"{endpoint}:{param_str}"

    # Hash if too long
    if len(key) > max_length:
        key_hash = hashlib.md5(key.encode()).hexdigest()
        return f"{endpoint}:hash:{key_hash}"

    return key


def format_error_response(
    error_code: int,
    message: str,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Format error response for MCP.

    Args:
        error_code: Error code
        message: Error message
        details: Optional error details

    Returns:
        Formatted error response
    """
    error_response = {
        "code": error_code,
        "message": message
    }

    if details:
        error_response["data"] = details

    return error_response


def format_health_response(
    status: str,
    services: Dict[str, Any],
    version: str = "1.0.0"
) -> Dict[str, Any]:
    """
    Format health check response.

    Args:
        status: Overall health status
        services: Service health details
        version: Server version

    Returns:
        Formatted health response
    """
    return {
        "status": status,
        "timestamp": datetime.utcnow().isoformat(),
        "services": services,
        "version": version
    }


def format_metrics_response(
    metrics: Dict[str, Any],
    format_type: str = "json"
) -> str:
    """
    Format metrics response.

    Args:
        metrics: Metrics data
        format_type: Output format (json or prometheus)

    Returns:
        Formatted metrics string
    """
    if format_type == "prometheus":
        return format_prometheus_metrics(metrics)
    else:
        return json.dumps(metrics, indent=2)


def format_prometheus_metrics(metrics: Dict[str, Any]) -> str:
    """
    Format metrics in Prometheus format.

    Args:
        metrics: Metrics data

    Returns:
        Prometheus formatted metrics
    """
    prometheus_lines = []

    # Add help and type comments
    prometheus_lines.extend([
        "# HELP news_mcp_requests_total Total number of requests",
        "# TYPE news_mcp_requests_total counter",
        f"news_mcp_requests_total {metrics.get('requests_total', 0)}",
        "",
        "# HELP news_mcp_cache_hits_total Total number of cache hits",
        "# TYPE news_mcp_cache_hits_total counter",
        f"news_mcp_cache_hits_total {metrics.get('cache_hits', 0)}",
        "",
        "# HELP news_mcp_response_time_seconds Average response time",
        "# TYPE news_mcp_response_time_seconds gauge",
        f"news_mcp_response_time_seconds {metrics.get('avg_response_time', 0)}",
        "",
        "# HELP news_mcp_errors_total Total number of errors",
        "# TYPE news_mcp_errors_total counter",
        f"news_mcp_errors_total {metrics.get('errors_total', 0)}",
        ""
    ])

    return "\n".join(prometheus_lines)


def sanitize_filename(filename: str, max_length: int = 255) -> str:
    """
    Sanitize filename for safe file operations.

    Args:
        filename: Original filename
        max_length: Maximum filename length

    Returns:
        Sanitized filename
    """
    import re

    # Remove or replace invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)

    # Remove control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32)

    # Trim length
    if len(sanitized) > max_length:
        name, ext = sanitized.rsplit('.', 1) if '.' in sanitized else (sanitized, '')
        available_length = max_length - len(ext) - 1 if ext else max_length
        sanitized = name[:available_length] + ('.' + ext if ext else '')

    return sanitized.strip()


def format_byte_size(size_bytes: int) -> str:
    """
    Format byte size in human-readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        Human-readable size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def format_duration(seconds: float) -> str:
    """
    Format duration in human-readable format.

    Args:
        seconds: Duration in seconds

    Returns:
        Human-readable duration string
    """
    if seconds < 1:
        return f"{seconds * 1000:.1f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    else:
        hours = seconds / 3600
        return f"{hours:.1f}h"