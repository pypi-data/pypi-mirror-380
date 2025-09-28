"""Helper utilities for News MCP Server."""

import asyncio
import logging
import time
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union
from datetime import datetime, timedelta


logger = logging.getLogger(__name__)

T = TypeVar('T')


async def async_retry(
    func: Callable[..., T],
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (Exception,),
    on_retry: Optional[Callable[[int, Exception], None]] = None
) -> T:
    """
    Retry an async function with exponential backoff.

    Args:
        func: Async function to retry
        max_attempts: Maximum number of attempts
        delay: Initial delay between attempts
        backoff_factor: Multiplier for delay on each retry
        exceptions: Tuple of exceptions to catch and retry
        on_retry: Optional callback called on each retry

    Returns:
        Result of the function call

    Raises:
        The last exception if all attempts fail
    """
    last_exception = None

    for attempt in range(max_attempts):
        try:
            if asyncio.iscoroutinefunction(func):
                return await func()
            else:
                return func()

        except exceptions as e:
            last_exception = e

            if attempt == max_attempts - 1:
                break

            if on_retry:
                on_retry(attempt + 1, e)

            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
            await asyncio.sleep(delay)
            delay *= backoff_factor

    raise last_exception


class RateLimiter:
    """Simple rate limiter implementation."""

    def __init__(self, max_requests: int, time_window: float):
        """
        Initialize rate limiter.

        Args:
            max_requests: Maximum requests allowed in time window
            time_window: Time window in seconds
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests: List[float] = []

    async def acquire(self) -> bool:
        """
        Acquire a rate limit slot.

        Returns:
            True if request allowed, False if rate limited
        """
        now = time.time()

        # Remove expired requests
        cutoff = now - self.time_window
        self.requests = [req_time for req_time in self.requests if req_time > cutoff]

        # Check if we can make a new request
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True

        return False

    async def wait_for_slot(self) -> None:
        """Wait until a rate limit slot becomes available."""
        while not await self.acquire():
            await asyncio.sleep(0.1)


def rate_limiter(max_requests: int, time_window: float):
    """
    Decorator for rate limiting async functions.

    Args:
        max_requests: Maximum requests allowed in time window
        time_window: Time window in seconds
    """
    limiter = RateLimiter(max_requests, time_window)

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            await limiter.wait_for_slot()
            return await func(*args, **kwargs)
        return wrapper
    return decorator


class CircuitBreaker:
    """Circuit breaker implementation for external services."""

    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 60.0,
        expected_exception: tuple = (Exception,)
    ):
        """
        Initialize circuit breaker.

        Args:
            failure_threshold: Number of failures before opening circuit
            recovery_timeout: Time to wait before attempting recovery
            expected_exception: Exceptions that count as failures
        """
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception

        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    async def call(self, func: Callable[..., T], *args, **kwargs) -> T:
        """
        Execute function with circuit breaker protection.

        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            Function result

        Raises:
            CircuitBreakerError: If circuit is open
            Original exception: If function fails
        """
        if self.state == "OPEN":
            if self._should_attempt_reset():
                self.state = "HALF_OPEN"
                logger.info("Circuit breaker entering HALF_OPEN state")
            else:
                raise CircuitBreakerError("Circuit breaker is OPEN")

        try:
            if asyncio.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)

            # Success - reset failure count
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                logger.info("Circuit breaker reset to CLOSED state")

            self.failure_count = 0
            return result

        except self.expected_exception as e:
            self._record_failure()
            raise e

    def _record_failure(self) -> None:
        """Record a failure and update circuit state."""
        self.failure_count += 1
        self.last_failure_time = datetime.utcnow()

        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"
            logger.warning(f"Circuit breaker OPENED after {self.failure_count} failures")

    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        if not self.last_failure_time:
            return True

        time_since_failure = (datetime.utcnow() - self.last_failure_time).total_seconds()
        return time_since_failure >= self.recovery_timeout


class CircuitBreakerError(Exception):
    """Exception raised when circuit breaker is open."""
    pass


def sanitize_text(
    text: str,
    max_length: Optional[int] = None,
    remove_html: bool = True,
    normalize_whitespace: bool = True
) -> str:
    """
    Sanitize text content.

    Args:
        text: Text to sanitize
        max_length: Maximum length to truncate to
        remove_html: Whether to remove HTML tags
        normalize_whitespace: Whether to normalize whitespace

    Returns:
        Sanitized text
    """
    if not isinstance(text, str):
        return ""

    sanitized = text

    # Remove HTML tags
    if remove_html:
        import re
        sanitized = re.sub(r'<[^>]+>', '', sanitized)

    # Normalize whitespace
    if normalize_whitespace:
        import re
        sanitized = re.sub(r'\s+', ' ', sanitized).strip()

    # Remove control characters except newlines and tabs
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\n\t')

    # Truncate if needed
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length].rstrip() + "..."

    return sanitized


class PerformanceTimer:
    """Context manager for measuring execution time."""

    def __init__(self, name: str = "operation"):
        self.name = name
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()

    @property
    def elapsed(self) -> float:
        """Get elapsed time in seconds."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0.0

    @property
    def elapsed_ms(self) -> float:
        """Get elapsed time in milliseconds."""
        return self.elapsed * 1000


async def async_timer(name: str = "operation"):
    """Async context manager for measuring execution time."""
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed = end_time - start_time
        logger.debug(f"{name} took {elapsed:.3f}s")


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """
    Split a list into chunks of specified size.

    Args:
        items: List to chunk
        chunk_size: Size of each chunk

    Returns:
        List of chunks
    """
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge multiple dictionaries, with later values taking precedence.

    Args:
        *dicts: Dictionaries to merge

    Returns:
        Merged dictionary
    """
    result = {}
    for d in dicts:
        if isinstance(d, dict):
            result.update(d)
    return result


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deep merge two dictionaries.

    Args:
        dict1: First dictionary
        dict2: Second dictionary (takes precedence)

    Returns:
        Deep merged dictionary
    """
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value

    return result


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate string to specified length with suffix.

    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add when truncating

    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text

    return text[:max_length - len(suffix)] + suffix


class AsyncBatch:
    """Utility for batching async operations."""

    def __init__(self, batch_size: int = 10, delay: float = 0.1):
        self.batch_size = batch_size
        self.delay = delay
        self.items = []

    async def add(self, item: Any) -> None:
        """Add item to batch."""
        self.items.append(item)

        if len(self.items) >= self.batch_size:
            await self.flush()

    async def flush(self) -> List[Any]:
        """Process and return current batch."""
        if not self.items:
            return []

        batch = self.items.copy()
        self.items.clear()

        # Small delay to prevent overwhelming downstream services
        if self.delay > 0:
            await asyncio.sleep(self.delay)

        return batch

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.flush()


def get_nested_value(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """
    Get value from nested dictionary using dot notation.

    Args:
        data: Dictionary to search
        path: Dot-separated path (e.g., "user.profile.name")
        default: Default value if path not found

    Returns:
        Value at path or default
    """
    keys = path.split('.')
    current = data

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current


def set_nested_value(data: Dict[str, Any], path: str, value: Any) -> None:
    """
    Set value in nested dictionary using dot notation.

    Args:
        data: Dictionary to modify
        path: Dot-separated path (e.g., "user.profile.name")
        value: Value to set
    """
    keys = path.split('.')
    current = data

    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value