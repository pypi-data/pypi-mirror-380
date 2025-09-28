"""Metrics collection and Prometheus integration."""

import time
import logging
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict, deque

from prometheus_client import (
    Counter, Histogram, Gauge, Info, CollectorRegistry,
    generate_latest, CONTENT_TYPE_LATEST
)


logger = logging.getLogger(__name__)


@dataclass
class RequestMetrics:
    """Request metrics data."""
    timestamp: datetime
    method: str
    endpoint: str
    status_code: int
    duration: float
    cached: bool = False
    error: Optional[str] = None


class MetricsCollector:
    """General metrics collector for the application."""

    def __init__(self, max_history: int = 10000):
        self.max_history = max_history
        self.request_history: deque = deque(maxlen=max_history)
        self.error_counts: Dict[str, int] = defaultdict(int)
        self.start_time = datetime.utcnow()

    def record_request(
        self,
        method: str,
        endpoint: str,
        status_code: int,
        duration: float,
        cached: bool = False,
        error: Optional[str] = None
    ) -> None:
        """Record a request metric."""
        metrics = RequestMetrics(
            timestamp=datetime.utcnow(),
            method=method,
            endpoint=endpoint,
            status_code=status_code,
            duration=duration,
            cached=cached,
            error=error
        )

        self.request_history.append(metrics)

        if error:
            self.error_counts[error] += 1

    def get_request_rate(self, window_minutes: int = 5) -> float:
        """Get request rate per minute for the given window."""
        cutoff = datetime.utcnow() - timedelta(minutes=window_minutes)
        recent_requests = [
            req for req in self.request_history
            if req.timestamp > cutoff
        ]
        return len(recent_requests) / window_minutes

    def get_error_rate(self, window_minutes: int = 5) -> float:
        """Get error rate percentage for the given window."""
        cutoff = datetime.utcnow() - timedelta(minutes=window_minutes)
        recent_requests = [
            req for req in self.request_history
            if req.timestamp > cutoff
        ]

        if not recent_requests:
            return 0.0

        error_requests = [req for req in recent_requests if req.status_code >= 400]
        return (len(error_requests) / len(recent_requests)) * 100

    def get_cache_hit_rate(self, window_minutes: int = 5) -> float:
        """Get cache hit rate percentage for the given window."""
        cutoff = datetime.utcnow() - timedelta(minutes=window_minutes)
        recent_requests = [
            req for req in self.request_history
            if req.timestamp > cutoff
        ]

        if not recent_requests:
            return 0.0

        cached_requests = [req for req in recent_requests if req.cached]
        return (len(cached_requests) / len(recent_requests)) * 100

    def get_average_response_time(self, window_minutes: int = 5) -> float:
        """Get average response time for the given window."""
        cutoff = datetime.utcnow() - timedelta(minutes=window_minutes)
        recent_requests = [
            req for req in self.request_history
            if req.timestamp > cutoff
        ]

        if not recent_requests:
            return 0.0

        total_duration = sum(req.duration for req in recent_requests)
        return total_duration / len(recent_requests)

    def get_uptime_seconds(self) -> float:
        """Get application uptime in seconds."""
        return (datetime.utcnow() - self.start_time).total_seconds()

    def get_summary_metrics(self) -> Dict[str, Any]:
        """Get summary of all metrics."""
        return {
            "uptime_seconds": self.get_uptime_seconds(),
            "total_requests": len(self.request_history),
            "request_rate_5m": self.get_request_rate(5),
            "error_rate_5m": self.get_error_rate(5),
            "cache_hit_rate_5m": self.get_cache_hit_rate(5),
            "avg_response_time_5m": self.get_average_response_time(5),
            "top_errors": dict(list(self.error_counts.items())[:5])
        }

    async def get_metrics(self) -> Dict[str, Any]:
        """Get metrics (async version for compatibility)."""
        return self.get_summary_metrics()

    def generate_prometheus_metrics(self) -> str:
        """Generate Prometheus formatted metrics."""
        metrics = self.get_summary_metrics()

        lines = [
            "# HELP news_mcp_requests_total Total number of requests",
            "# TYPE news_mcp_requests_total counter",
            f"news_mcp_requests_total {metrics['total_requests']}",
            "",
            "# HELP news_mcp_uptime_seconds Server uptime in seconds",
            "# TYPE news_mcp_uptime_seconds gauge",
            f"news_mcp_uptime_seconds {metrics['uptime_seconds']}",
            "",
            "# HELP news_mcp_request_rate_5m Request rate per minute over 5 minutes",
            "# TYPE news_mcp_request_rate_5m gauge",
            f"news_mcp_request_rate_5m {metrics['request_rate_5m']}",
            "",
            "# HELP news_mcp_error_rate_5m Error rate percentage over 5 minutes",
            "# TYPE news_mcp_error_rate_5m gauge",
            f"news_mcp_error_rate_5m {metrics['error_rate_5m']}",
            "",
            "# HELP news_mcp_cache_hit_rate_5m Cache hit rate percentage over 5 minutes",
            "# TYPE news_mcp_cache_hit_rate_5m gauge",
            f"news_mcp_cache_hit_rate_5m {metrics['cache_hit_rate_5m']}",
            "",
            "# HELP news_mcp_avg_response_time_5m Average response time over 5 minutes",
            "# TYPE news_mcp_avg_response_time_5m gauge",
            f"news_mcp_avg_response_time_5m {metrics['avg_response_time_5m']}",
            ""
        ]

        return "\n".join(lines)


class PrometheusMetrics:
    """Prometheus metrics integration."""

    def __init__(self, registry: Optional[CollectorRegistry] = None):
        self.registry = registry or CollectorRegistry()

        # Define metrics
        self.request_count = Counter(
            'news_mcp_requests_total',
            'Total number of requests',
            ['method', 'endpoint', 'status'],
            registry=self.registry
        )

        self.request_duration = Histogram(
            'news_mcp_request_duration_seconds',
            'Request duration in seconds',
            ['method', 'endpoint'],
            registry=self.registry
        )

        self.cache_operations = Counter(
            'news_mcp_cache_operations_total',
            'Total cache operations',
            ['operation', 'result'],
            registry=self.registry
        )

        self.active_connections = Gauge(
            'news_mcp_active_connections',
            'Number of active connections',
            registry=self.registry
        )

        self.news_api_requests = Counter(
            'news_mcp_news_api_requests_total',
            'Total requests to news APIs',
            ['api', 'method', 'status'],
            registry=self.registry
        )

        self.news_api_credits = Counter(
            'news_mcp_news_api_credits_total',
            'Total API credits consumed',
            ['api'],
            registry=self.registry
        )

        self.plugin_operations = Counter(
            'news_mcp_plugin_operations_total',
            'Total plugin operations',
            ['plugin', 'operation', 'status'],
            registry=self.registry
        )

        # Application info
        self.app_info = Info(
            'news_mcp_app',
            'Application information',
            registry=self.registry
        )

        # Set application info
        self.app_info.info({
            'version': '1.0.0',
            'name': 'news-mcp-server',
            'framework': 'fastapi'
        })

    def record_request(
        self,
        method: str,
        endpoint: str,
        status_code: int,
        duration: float
    ) -> None:
        """Record request metrics."""
        status_range = f"{status_code // 100}xx"

        self.request_count.labels(
            method=method,
            endpoint=endpoint,
            status=status_range
        ).inc()

        self.request_duration.labels(
            method=method,
            endpoint=endpoint
        ).observe(duration)

    def record_cache_operation(self, operation: str, result: str) -> None:
        """Record cache operation."""
        self.cache_operations.labels(
            operation=operation,
            result=result
        ).inc()

    def set_active_connections(self, count: int) -> None:
        """Set active connections count."""
        self.active_connections.set(count)

    def record_news_api_request(self, api: str, method: str, status_code: int) -> None:
        """Record news API request."""
        status_range = f"{status_code // 100}xx"
        self.news_api_requests.labels(
            api=api,
            method=method,
            status=status_range
        ).inc()

    def record_news_api_credits(self, api: str, credits: int) -> None:
        """Record news API credits usage."""
        self.news_api_credits.labels(api=api).inc(credits)

    def record_plugin_operation(self, plugin: str, operation: str, success: bool) -> None:
        """Record plugin operation."""
        status = "success" if success else "error"
        self.plugin_operations.labels(
            plugin=plugin,
            operation=operation,
            status=status
        ).inc()

    def generate_metrics(self) -> bytes:
        """Generate Prometheus metrics output."""
        return generate_latest(self.registry)

    def get_content_type(self) -> str:
        """Get Prometheus content type."""
        return CONTENT_TYPE_LATEST


class MetricsMiddleware:
    """FastAPI middleware for collecting metrics."""

    def __init__(
        self,
        metrics_collector: MetricsCollector,
        prometheus_metrics: PrometheusMetrics
    ):
        self.metrics_collector = metrics_collector
        self.prometheus_metrics = prometheus_metrics

    async def __call__(self, request, call_next):
        """Process request and collect metrics."""
        start_time = time.time()
        method = request.method
        endpoint = request.url.path

        # Check if response is from cache
        cached = getattr(request.state, 'cached', False)

        try:
            response = await call_next(request)
            status_code = response.status_code
            error = None

        except Exception as e:
            status_code = 500
            error = str(e)
            raise

        finally:
            # Calculate duration
            duration = time.time() - start_time

            # Record metrics
            self.metrics_collector.record_request(
                method=method,
                endpoint=endpoint,
                status_code=status_code,
                duration=duration,
                cached=cached,
                error=error
            )

            self.prometheus_metrics.record_request(
                method=method,
                endpoint=endpoint,
                status_code=status_code,
                duration=duration
            )

        return response


class MetricsExporter:
    """Export metrics to various formats."""

    def __init__(self, metrics_collector: MetricsCollector):
        self.metrics_collector = metrics_collector

    def export_json(self) -> Dict[str, Any]:
        """Export metrics as JSON."""
        return self.metrics_collector.get_summary_metrics()

    def export_csv(self) -> str:
        """Export request history as CSV."""
        import csv
        import io

        output = io.StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow([
            'timestamp', 'method', 'endpoint', 'status_code',
            'duration', 'cached', 'error'
        ])

        # Data
        for req in self.metrics_collector.request_history:
            writer.writerow([
                req.timestamp.isoformat(),
                req.method,
                req.endpoint,
                req.status_code,
                req.duration,
                req.cached,
                req.error or ''
            ])

        return output.getvalue()

    def export_histogram_data(self, window_minutes: int = 60) -> Dict[str, List[float]]:
        """Export histogram data for visualization."""
        cutoff = datetime.utcnow() - timedelta(minutes=window_minutes)
        recent_requests = [
            req for req in self.metrics_collector.request_history
            if req.timestamp > cutoff
        ]

        # Group by endpoint
        endpoint_durations = defaultdict(list)
        for req in recent_requests:
            endpoint_durations[req.endpoint].append(req.duration)

        return dict(endpoint_durations)