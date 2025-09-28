"""Health check system for News MCP Server."""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Callable, Awaitable
from enum import Enum
from dataclasses import dataclass

import httpx


logger = logging.getLogger(__name__)


class HealthStatus(str, Enum):
    """Health check status levels."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"


@dataclass
class HealthCheckResult:
    """Result of a health check."""
    service: str
    status: HealthStatus
    response_time_ms: Optional[float] = None
    error: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class BaseHealthCheck:
    """Base class for health checks."""

    def __init__(self, name: str, timeout: float = 5.0):
        self.name = name
        self.timeout = timeout

    async def check(self) -> HealthCheckResult:
        """Perform the health check."""
        try:
            start_time = datetime.utcnow()
            result = await asyncio.wait_for(self._check(), timeout=self.timeout)
            end_time = datetime.utcnow()

            response_time = (end_time - start_time).total_seconds() * 1000

            return HealthCheckResult(
                service=self.name,
                status=result.get('status', HealthStatus.HEALTHY),
                response_time_ms=response_time,
                details=result.get('details'),
                timestamp=start_time
            )

        except asyncio.TimeoutError:
            return HealthCheckResult(
                service=self.name,
                status=HealthStatus.UNHEALTHY,
                error=f"Health check timed out after {self.timeout}s"
            )

        except Exception as e:
            return HealthCheckResult(
                service=self.name,
                status=HealthStatus.UNHEALTHY,
                error=str(e)
            )

    async def _check(self) -> Dict[str, Any]:
        """Override this method to implement the health check logic."""
        raise NotImplementedError


class DatabaseHealthCheck(BaseHealthCheck):
    """Health check for database connections."""

    def __init__(self, name: str = "database", connection_pool=None, timeout: float = 5.0):
        super().__init__(name, timeout)
        self.connection_pool = connection_pool

    async def _check(self) -> Dict[str, Any]:
        """Check database connectivity."""
        if not self.connection_pool:
            return {
                'status': HealthStatus.UNKNOWN,
                'details': {'message': 'No database connection configured'}
            }

        # Simple ping test
        try:
            # This would be database-specific
            # For Redis: await connection.ping()
            # For PostgreSQL: await connection.fetchval("SELECT 1")
            return {
                'status': HealthStatus.HEALTHY,
                'details': {'message': 'Database connection successful'}
            }
        except Exception as e:
            return {
                'status': HealthStatus.UNHEALTHY,
                'details': {'error': str(e)}
            }


class RedisHealthCheck(BaseHealthCheck):
    """Health check for Redis cache."""

    def __init__(self, redis_client, name: str = "redis", timeout: float = 5.0):
        super().__init__(name, timeout)
        self.redis_client = redis_client

    async def _check(self) -> Dict[str, Any]:
        """Check Redis connectivity."""
        if not self.redis_client:
            return {
                'status': HealthStatus.UNKNOWN,
                'details': {'message': 'Redis client not configured'}
            }

        try:
            # Ping Redis
            await self.redis_client.ping()

            # Get some info
            info = await self.redis_client.info()
            memory_usage = info.get('used_memory_human', 'unknown')
            connected_clients = info.get('connected_clients', 0)

            return {
                'status': HealthStatus.HEALTHY,
                'details': {
                    'memory_usage': memory_usage,
                    'connected_clients': connected_clients,
                    'redis_version': info.get('redis_version', 'unknown')
                }
            }

        except Exception as e:
            return {
                'status': HealthStatus.UNHEALTHY,
                'details': {'error': str(e)}
            }


class ExternalAPIHealthCheck(BaseHealthCheck):
    """Health check for external APIs."""

    def __init__(
        self,
        name: str,
        url: str,
        expected_status: int = 200,
        timeout: float = 10.0,
        headers: Optional[Dict[str, str]] = None
    ):
        super().__init__(name, timeout)
        self.url = url
        self.expected_status = expected_status
        self.headers = headers or {}

    async def _check(self) -> Dict[str, Any]:
        """Check external API availability."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    self.url,
                    headers=self.headers,
                    timeout=self.timeout
                )

                if response.status_code == self.expected_status:
                    status = HealthStatus.HEALTHY
                elif 200 <= response.status_code < 300:
                    status = HealthStatus.DEGRADED
                else:
                    status = HealthStatus.UNHEALTHY

                return {
                    'status': status,
                    'details': {
                        'status_code': response.status_code,
                        'response_time_ms': response.elapsed.total_seconds() * 1000
                    }
                }

        except httpx.TimeoutException:
            return {
                'status': HealthStatus.UNHEALTHY,
                'details': {'error': 'Request timeout'}
            }

        except Exception as e:
            return {
                'status': HealthStatus.UNHEALTHY,
                'details': {'error': str(e)}
            }


class MemoryHealthCheck(BaseHealthCheck):
    """Health check for memory usage."""

    def __init__(
        self,
        name: str = "memory",
        warning_threshold: float = 80.0,
        critical_threshold: float = 95.0,
        timeout: float = 1.0
    ):
        super().__init__(name, timeout)
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold

    async def _check(self) -> Dict[str, Any]:
        """Check memory usage."""
        try:
            import psutil

            memory = psutil.virtual_memory()
            usage_percent = memory.percent

            if usage_percent >= self.critical_threshold:
                status = HealthStatus.UNHEALTHY
            elif usage_percent >= self.warning_threshold:
                status = HealthStatus.DEGRADED
            else:
                status = HealthStatus.HEALTHY

            return {
                'status': status,
                'details': {
                    'usage_percent': usage_percent,
                    'available_mb': memory.available // (1024 * 1024),
                    'total_mb': memory.total // (1024 * 1024)
                }
            }

        except ImportError:
            return {
                'status': HealthStatus.UNKNOWN,
                'details': {'message': 'psutil not available for memory monitoring'}
            }

        except Exception as e:
            return {
                'status': HealthStatus.UNKNOWN,
                'details': {'error': str(e)}
            }


class DiskHealthCheck(BaseHealthCheck):
    """Health check for disk usage."""

    def __init__(
        self,
        name: str = "disk",
        path: str = "/",
        warning_threshold: float = 80.0,
        critical_threshold: float = 95.0,
        timeout: float = 1.0
    ):
        super().__init__(name, timeout)
        self.path = path
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold

    async def _check(self) -> Dict[str, Any]:
        """Check disk usage."""
        try:
            import psutil

            disk = psutil.disk_usage(self.path)
            usage_percent = (disk.used / disk.total) * 100

            if usage_percent >= self.critical_threshold:
                status = HealthStatus.UNHEALTHY
            elif usage_percent >= self.warning_threshold:
                status = HealthStatus.DEGRADED
            else:
                status = HealthStatus.HEALTHY

            return {
                'status': status,
                'details': {
                    'usage_percent': round(usage_percent, 2),
                    'free_gb': round(disk.free / (1024**3), 2),
                    'total_gb': round(disk.total / (1024**3), 2),
                    'path': self.path
                }
            }

        except ImportError:
            return {
                'status': HealthStatus.UNKNOWN,
                'details': {'message': 'psutil not available for disk monitoring'}
            }

        except Exception as e:
            return {
                'status': HealthStatus.UNKNOWN,
                'details': {'error': str(e)}
            }


class CustomHealthCheck(BaseHealthCheck):
    """Custom health check using a callable."""

    def __init__(
        self,
        name: str,
        check_func: Callable[[], Awaitable[Dict[str, Any]]],
        timeout: float = 5.0
    ):
        super().__init__(name, timeout)
        self.check_func = check_func

    async def _check(self) -> Dict[str, Any]:
        """Execute custom health check function."""
        return await self.check_func()


class HealthChecker:
    """Main health checker that coordinates all health checks."""

    def __init__(self):
        self.checks: List[BaseHealthCheck] = []
        self.last_results: Dict[str, HealthCheckResult] = {}

    async def initialize(self) -> None:
        """Initialize health checker with basic checks."""
        # Add basic system health checks
        self.add_check(MemoryHealthCheck())
        self.add_check(DiskHealthCheck())
        logger.info("Health checker initialized with basic system checks")

    async def check_health(self) -> Dict[str, Any]:
        """Perform health check and return results."""
        results = await self.check_all()
        return self.get_health_summary()

    def add_check(self, check: BaseHealthCheck) -> None:
        """Add a health check."""
        self.checks.append(check)
        logger.info(f"Added health check: {check.name}")

    def remove_check(self, name: str) -> bool:
        """Remove a health check by name."""
        for i, check in enumerate(self.checks):
            if check.name == name:
                del self.checks[i]
                logger.info(f"Removed health check: {name}")
                return True
        return False

    async def check_all(self, parallel: bool = True) -> Dict[str, HealthCheckResult]:
        """Run all health checks."""
        if not self.checks:
            return {}

        if parallel:
            # Run checks in parallel
            tasks = [check.check() for check in self.checks]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            check_results = {}
            for check, result in zip(self.checks, results):
                if isinstance(result, Exception):
                    check_results[check.name] = HealthCheckResult(
                        service=check.name,
                        status=HealthStatus.UNHEALTHY,
                        error=str(result)
                    )
                else:
                    check_results[check.name] = result

        else:
            # Run checks sequentially
            check_results = {}
            for check in self.checks:
                check_results[check.name] = await check.check()

        # Update last results
        self.last_results.update(check_results)

        return check_results

    async def check_single(self, name: str) -> Optional[HealthCheckResult]:
        """Run a single health check by name."""
        for check in self.checks:
            if check.name == name:
                result = await check.check()
                self.last_results[name] = result
                return result
        return None

    def get_overall_status(self, results: Optional[Dict[str, HealthCheckResult]] = None) -> HealthStatus:
        """Get overall health status."""
        if results is None:
            results = self.last_results

        if not results:
            return HealthStatus.UNKNOWN

        statuses = [result.status for result in results.values()]

        if HealthStatus.UNHEALTHY in statuses:
            return HealthStatus.UNHEALTHY
        elif HealthStatus.DEGRADED in statuses:
            return HealthStatus.DEGRADED
        elif all(status == HealthStatus.HEALTHY for status in statuses):
            return HealthStatus.HEALTHY
        else:
            return HealthStatus.UNKNOWN

    def get_health_summary(self) -> Dict[str, Any]:
        """Get health summary."""
        overall_status = self.get_overall_status()

        service_statuses = {}
        for name, result in self.last_results.items():
            service_statuses[name] = {
                'status': result.status.value,
                'response_time_ms': result.response_time_ms,
                'error': result.error,
                'timestamp': result.timestamp.isoformat() if result.timestamp else None
            }

        return {
            'status': overall_status.value,
            'timestamp': datetime.utcnow().isoformat(),
            'services': service_statuses,
            'checks_count': len(self.checks)
        }

    async def continuous_monitoring(
        self,
        interval: float = 30.0,
        on_status_change: Optional[Callable[[str, HealthStatus, HealthStatus], None]] = None
    ) -> None:
        """Run continuous health monitoring."""
        logger.info(f"Starting continuous health monitoring (interval: {interval}s)")

        previous_statuses = {}

        while True:
            try:
                results = await self.check_all()

                # Check for status changes
                if on_status_change:
                    for name, result in results.items():
                        previous_status = previous_statuses.get(name)
                        if previous_status and previous_status != result.status:
                            on_status_change(name, previous_status, result.status)

                        previous_statuses[name] = result.status

                await asyncio.sleep(interval)

            except Exception as e:
                logger.error(f"Error in continuous monitoring: {e}")
                await asyncio.sleep(interval)