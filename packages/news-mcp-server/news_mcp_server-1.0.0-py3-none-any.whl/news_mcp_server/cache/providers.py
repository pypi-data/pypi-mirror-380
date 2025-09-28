"""Cache provider implementations."""

import json
import logging
import hashlib
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union
from datetime import datetime, timedelta

import redis.asyncio as redis
from redis.asyncio import ConnectionPool


logger = logging.getLogger(__name__)


class CacheProvider(ABC):
    """Abstract cache provider interface."""

    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        pass

    @abstractmethod
    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Set value in cache with optional TTL."""
        pass

    @abstractmethod
    async def delete(self, key: str) -> bool:
        """Delete value from cache."""
        pass

    @abstractmethod
    async def exists(self, key: str) -> bool:
        """Check if key exists in cache."""
        pass

    @abstractmethod
    async def clear(self) -> bool:
        """Clear all cache entries."""
        pass

    @abstractmethod
    async def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        pass

    @abstractmethod
    async def health_check(self) -> Dict[str, Any]:
        """Perform cache health check."""
        pass

    def make_key(self, prefix: str, **kwargs) -> str:
        """Create cache key from parameters."""
        # Sort kwargs for consistent key generation
        sorted_items = sorted(kwargs.items())
        key_data = f"{prefix}:" + ":".join(f"{k}={v}" for k, v in sorted_items)

        # Hash long keys to avoid Redis key length limits
        if len(key_data) > 200:
            key_hash = hashlib.md5(key_data.encode()).hexdigest()
            return f"{prefix}:hashed:{key_hash}"

        return key_data


class RedisProvider(CacheProvider):
    """Redis cache provider."""

    def __init__(
        self,
        redis_url: str = "redis://localhost:6379/0",
        max_connections: int = 10,
        **kwargs
    ):
        self.redis_url = redis_url
        self.max_connections = max_connections
        self.pool: Optional[ConnectionPool] = None
        self.client: Optional[redis.Redis] = None
        self._stats = {
            "hits": 0,
            "misses": 0,
            "sets": 0,
            "deletes": 0,
            "errors": 0,
        }

    async def connect(self) -> None:
        """Initialize Redis connection."""
        try:
            self.pool = ConnectionPool.from_url(
                self.redis_url,
                max_connections=self.max_connections,
                decode_responses=True,
            )
            self.client = redis.Redis(connection_pool=self.pool)

            # Test connection
            await self.client.ping()
            logger.info("Redis cache provider connected successfully")

        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            self._stats["errors"] += 1
            raise

    async def disconnect(self) -> None:
        """Close Redis connection."""
        if self.client:
            await self.client.close()
        if self.pool:
            await self.pool.disconnect()

    async def get(self, key: str) -> Optional[Any]:
        """Get value from Redis cache."""
        if not self.client:
            await self.connect()

        try:
            value = await self.client.get(key)
            if value is not None:
                self._stats["hits"] += 1
                return json.loads(value)
            else:
                self._stats["misses"] += 1
                return None

        except Exception as e:
            logger.error(f"Cache get error for key {key}: {e}")
            self._stats["errors"] += 1
            return None

    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Set value in Redis cache."""
        if not self.client:
            await self.connect()

        try:
            serialized_value = json.dumps(value, default=str)

            if ttl:
                result = await self.client.setex(key, ttl, serialized_value)
            else:
                result = await self.client.set(key, serialized_value)

            if result:
                self._stats["sets"] += 1
                return True
            return False

        except Exception as e:
            logger.error(f"Cache set error for key {key}: {e}")
            self._stats["errors"] += 1
            return False

    async def delete(self, key: str) -> bool:
        """Delete value from Redis cache."""
        if not self.client:
            await self.connect()

        try:
            result = await self.client.delete(key)
            if result > 0:
                self._stats["deletes"] += 1
                return True
            return False

        except Exception as e:
            logger.error(f"Cache delete error for key {key}: {e}")
            self._stats["errors"] += 1
            return False

    async def exists(self, key: str) -> bool:
        """Check if key exists in Redis cache."""
        if not self.client:
            await self.connect()

        try:
            result = await self.client.exists(key)
            return result > 0

        except Exception as e:
            logger.error(f"Cache exists error for key {key}: {e}")
            self._stats["errors"] += 1
            return False

    async def clear(self) -> bool:
        """Clear all cache entries."""
        if not self.client:
            await self.connect()

        try:
            await self.client.flushdb()
            return True

        except Exception as e:
            logger.error(f"Cache clear error: {e}")
            self._stats["errors"] += 1
            return False

    async def get_stats(self) -> Dict[str, Any]:
        """Get Redis cache statistics."""
        stats = self._stats.copy()

        if self.client:
            try:
                info = await self.client.info()
                stats.update({
                    "redis_version": info.get("redis_version"),
                    "used_memory": info.get("used_memory_human"),
                    "connected_clients": info.get("connected_clients"),
                    "total_commands_processed": info.get("total_commands_processed"),
                })
            except Exception as e:
                logger.error(f"Error getting Redis stats: {e}")

        # Calculate hit rate
        total_gets = stats["hits"] + stats["misses"]
        stats["hit_rate"] = stats["hits"] / total_gets if total_gets > 0 else 0.0

        return stats

    async def health_check(self) -> Dict[str, Any]:
        """Perform Redis health check."""
        if not self.client:
            return {"status": "disconnected", "error": "No connection"}

        try:
            start_time = datetime.utcnow()
            await self.client.ping()
            response_time = (datetime.utcnow() - start_time).total_seconds()

            return {
                "status": "healthy",
                "response_time_ms": response_time * 1000,
                "url": self.redis_url.split("@")[-1] if "@" in self.redis_url else self.redis_url,
            }

        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
            }


class MemoryProvider(CacheProvider):
    """In-memory cache provider for development/testing."""

    def __init__(self, max_size: int = 1000):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.max_size = max_size
        self._stats = {
            "hits": 0,
            "misses": 0,
            "sets": 0,
            "deletes": 0,
            "evictions": 0,
        }

    async def get(self, key: str) -> Optional[Any]:
        """Get value from memory cache."""
        if key in self.cache:
            entry = self.cache[key]

            # Check if expired
            if entry["expires_at"] and datetime.utcnow() > entry["expires_at"]:
                del self.cache[key]
                self._stats["misses"] += 1
                return None

            self._stats["hits"] += 1
            return entry["value"]

        self._stats["misses"] += 1
        return None

    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Set value in memory cache."""
        try:
            # Evict oldest entries if at max size
            if len(self.cache) >= self.max_size and key not in self.cache:
                self._evict_oldest()

            expires_at = None
            if ttl:
                expires_at = datetime.utcnow() + timedelta(seconds=ttl)

            self.cache[key] = {
                "value": value,
                "expires_at": expires_at,
                "created_at": datetime.utcnow(),
            }

            self._stats["sets"] += 1
            return True

        except Exception as e:
            logger.error(f"Memory cache set error: {e}")
            return False

    async def delete(self, key: str) -> bool:
        """Delete value from memory cache."""
        if key in self.cache:
            del self.cache[key]
            self._stats["deletes"] += 1
            return True
        return False

    async def exists(self, key: str) -> bool:
        """Check if key exists in memory cache."""
        if key in self.cache:
            entry = self.cache[key]
            # Check if expired
            if entry["expires_at"] and datetime.utcnow() > entry["expires_at"]:
                del self.cache[key]
                return False
            return True
        return False

    async def clear(self) -> bool:
        """Clear all cache entries."""
        self.cache.clear()
        return True

    def _evict_oldest(self) -> None:
        """Evict oldest cache entry."""
        if not self.cache:
            return

        oldest_key = min(
            self.cache.keys(),
            key=lambda k: self.cache[k]["created_at"]
        )
        del self.cache[oldest_key]
        self._stats["evictions"] += 1

    async def get_stats(self) -> Dict[str, Any]:
        """Get memory cache statistics."""
        stats = self._stats.copy()

        # Calculate hit rate
        total_gets = stats["hits"] + stats["misses"]
        stats["hit_rate"] = stats["hits"] / total_gets if total_gets > 0 else 0.0

        # Add memory usage info
        stats.update({
            "entries": len(self.cache),
            "max_size": self.max_size,
            "memory_usage_percent": len(self.cache) / self.max_size * 100,
        })

        return stats

    async def health_check(self) -> Dict[str, Any]:
        """Perform memory cache health check."""
        return {
            "status": "healthy",
            "provider": "memory",
            "entries": len(self.cache),
            "max_size": self.max_size,
        }