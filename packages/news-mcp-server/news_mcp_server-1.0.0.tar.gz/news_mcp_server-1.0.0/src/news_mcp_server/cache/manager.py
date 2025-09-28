"""Cache manager for coordinating cache operations."""

import logging
from typing import Any, Dict, Optional, Type

from ..core.config import CacheConfig
from .providers import CacheProvider, RedisProvider, MemoryProvider


logger = logging.getLogger(__name__)


class CacheManager:
    """Cache manager that coordinates cache operations."""

    def __init__(self, config: CacheConfig):
        self.config = config
        self.provider: Optional[CacheProvider] = None
        self._initialized = False

    async def initialize(self) -> None:
        """Initialize cache provider."""
        if self._initialized:
            return

        if not self.config.enabled:
            logger.info("Cache is disabled")
            return

        try:
            if self.config.provider == "redis":
                self.provider = RedisProvider(
                    redis_url=self.config.redis_url,
                    max_connections=self.config.max_connections,
                )
                if hasattr(self.provider, 'connect'):
                    await self.provider.connect()

            elif self.config.provider == "memory":
                self.provider = MemoryProvider(max_size=1000)

            else:
                raise ValueError(f"Unknown cache provider: {self.config.provider}")

            self._initialized = True
            logger.info(f"Cache manager initialized with {self.config.provider} provider")

        except Exception as e:
            logger.error(f"Failed to initialize cache: {e}")
            # Fall back to memory cache
            self.provider = MemoryProvider(max_size=100)
            self._initialized = True
            logger.info("Fallback to memory cache due to initialization error")

    async def close(self) -> None:
        """Shutdown cache provider."""
        if self.provider and hasattr(self.provider, 'disconnect'):
            await self.provider.disconnect()

    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if not self._is_enabled():
            return None
        return await self.provider.get(key)

    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Set value in cache."""
        if not self._is_enabled():
            return False
        cache_ttl = ttl or self.config.ttl
        return await self.provider.set(key, value, cache_ttl)

    async def get_headlines(
        self,
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20
    ) -> Optional[Dict[str, Any]]:
        """Get cached news headlines."""
        if not self._is_enabled():
            return None

        cache_key = self.provider.make_key(
            "headlines",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        return await self.provider.get(cache_key)

    async def set_headlines(
        self,
        data: Dict[str, Any],
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        ttl: Optional[int] = None
    ) -> bool:
        """Cache news headlines."""
        if not self._is_enabled():
            return False

        cache_key = self.provider.make_key(
            "headlines",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        cache_ttl = ttl or self.config.ttl
        return await self.provider.set(cache_key, data, cache_ttl)

    async def get_briefs(
        self,
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20
    ) -> Optional[Dict[str, Any]]:
        """Get cached news briefs."""
        if not self._is_enabled():
            return None

        cache_key = self.provider.make_key(
            "briefs",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        return await self.provider.get(cache_key)

    async def set_briefs(
        self,
        data: Dict[str, Any],
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        ttl: Optional[int] = None
    ) -> bool:
        """Cache news briefs."""
        if not self._is_enabled():
            return False

        cache_key = self.provider.make_key(
            "briefs",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        cache_ttl = ttl or self.config.ttl
        return await self.provider.set(cache_key, data, cache_ttl)

    async def get_fulltext(
        self,
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20
    ) -> Optional[Dict[str, Any]]:
        """Get cached full text news."""
        if not self._is_enabled():
            return None

        cache_key = self.provider.make_key(
            "fulltext",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        return await self.provider.get(cache_key)

    async def set_fulltext(
        self,
        data: Dict[str, Any],
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        ttl: Optional[int] = None
    ) -> bool:
        """Cache full text news."""
        if not self._is_enabled():
            return False

        cache_key = self.provider.make_key(
            "fulltext",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        cache_ttl = ttl or self.config.ttl
        return await self.provider.set(cache_key, data, cache_ttl)

    async def get_metadata(
        self,
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20
    ) -> Optional[Dict[str, Any]]:
        """Get cached metadata news."""
        if not self._is_enabled():
            return None

        cache_key = self.provider.make_key(
            "metadata",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        return await self.provider.get(cache_key)

    async def set_metadata(
        self,
        data: Dict[str, Any],
        query_text: str,
        country_code: Optional[str] = None,
        lang_code: Optional[str] = None,
        sort: str = "latest",
        count: int = 20,
        ttl: Optional[int] = None
    ) -> bool:
        """Cache metadata news."""
        if not self._is_enabled():
            return False

        cache_key = self.provider.make_key(
            "metadata",
            query=query_text,
            country=country_code or "all",
            lang=lang_code or "all",
            sort=sort,
            count=count
        )

        cache_ttl = ttl or self.config.ttl
        return await self.provider.set(cache_key, data, cache_ttl)

    async def invalidate_pattern(self, pattern: str) -> int:
        """Invalidate cache entries matching pattern."""
        if not self._is_enabled():
            return 0

        # This is a simplified implementation
        # In production, you'd want to use Redis SCAN with pattern matching
        logger.warning(f"Pattern invalidation not fully implemented: {pattern}")
        return 0

    async def clear_all(self) -> bool:
        """Clear all cache entries."""
        if not self._is_enabled():
            return True

        return await self.provider.clear()

    async def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        if not self._is_enabled():
            return {"enabled": False}

        stats = await self.provider.get_stats()
        stats["enabled"] = True
        stats["provider"] = self.config.provider
        stats["ttl"] = self.config.ttl
        return stats

    async def health_check(self) -> Dict[str, Any]:
        """Perform cache health check."""
        if not self._is_enabled():
            return {"status": "disabled"}

        return await self.provider.health_check()

    def _is_enabled(self) -> bool:
        """Check if cache is enabled and initialized."""
        return self.config.enabled and self._initialized and self.provider is not None