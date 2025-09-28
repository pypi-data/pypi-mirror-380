"""Redis storage backends for aiogram-sentinel."""

from __future__ import annotations

import time
from typing import Any

from redis.asyncio import Redis
from redis.exceptions import RedisError

from ..exceptions import BackendOperationError
from .base import BlocklistBackend, DebounceBackend, RateLimiterBackend, UserRepo


def _k(prefix: str, *parts: str) -> str:
    """Build namespaced Redis key."""
    return f"{prefix}:{':'.join(parts)}"


class RedisRateLimiter(RateLimiterBackend):
    """Redis rate limiter using INCR + EXPIRE pattern."""

    def __init__(self, redis: Redis, prefix: str) -> None:
        """Initialize the rate limiter."""
        self._redis = redis
        self._prefix = prefix

    async def allow(self, key: str, max_events: int, per_seconds: int) -> bool:
        """Check if request is allowed and increment counter."""
        try:
            redis_key = _k(self._prefix, "rate", key)
            # Use pipeline for atomic operation
            pipe = self._redis.pipeline()
            pipe.incr(redis_key)
            pipe.ttl(redis_key)
            count, ttl = await pipe.execute()
            if ttl == -1:  # Set TTL if absent
                await self._redis.expire(redis_key, per_seconds)
            return int(count) <= max_events
        except RedisError as e:
            raise BackendOperationError(f"Failed to check rate limit: {e}") from e

    async def get_remaining(self, key: str, max_events: int, per_seconds: int) -> int:
        """Get remaining requests in current window."""
        try:
            redis_key = _k(self._prefix, "rate", key)
            val = await self._redis.get(redis_key)
            return max(0, max_events - int(val or 0))
        except RedisError as e:
            raise BackendOperationError(f"Failed to get remaining: {e}") from e


class RedisDebounce(DebounceBackend):
    """Redis debounce backend using SET NX EX pattern."""

    def __init__(self, redis: Redis, prefix: str) -> None:
        """Initialize the debounce backend."""
        self._redis = redis
        self._prefix = prefix

    async def seen(self, key: str, window_seconds: int, fingerprint: str) -> bool:
        """Check if fingerprint was seen within window and record it."""
        try:
            fp = fingerprint  # Use fingerprint directly
            k = _k(self._prefix, "debounce", key, fp)
            added = await self._redis.set(
                k, int(time.time()), ex=window_seconds, nx=True
            )
            # nx=True => returns True if set, None if exists
            return added is None
        except RedisError as e:
            raise BackendOperationError(f"Failed to check debounce: {e}") from e


class RedisBlocklist(BlocklistBackend):
    """Redis blocklist backend using SADD/SREM/SISMEMBER."""

    def __init__(self, redis: Redis, prefix: str) -> None:
        """Initialize the blocklist backend."""
        self._redis = redis
        self._prefix = prefix
        self._blocklist_key = _k(self._prefix, "blocklist")

    async def is_blocked(self, user_id: int) -> bool:
        """Check if user is blocked."""
        try:
            result = await self._redis.sismember(self._blocklist_key, str(user_id))  # type: ignore
            return bool(result)  # type: ignore
        except RedisError as e:
            raise BackendOperationError(f"Failed to check blocklist: {e}") from e

    async def set_blocked(self, user_id: int, blocked: bool) -> None:
        """Set user blocked status."""
        try:
            if blocked:
                await self._redis.sadd(self._blocklist_key, str(user_id))  # type: ignore
            else:
                await self._redis.srem(self._blocklist_key, str(user_id))  # type: ignore
        except RedisError as e:
            raise BackendOperationError(f"Failed to set blocked status: {e}") from e


class RedisUserRepo(UserRepo):
    """Redis user repository using HSETNX/HSET."""

    def __init__(self, redis: Redis, prefix: str) -> None:
        """Initialize the user repository."""
        self._redis = redis
        self._prefix = prefix

    async def ensure_user(self, user_id: int, *, username: str | None = None) -> None:
        """Ensure user exists, creating if necessary."""
        try:
            redis_key = _k(self._prefix, "user", str(user_id))
            await self._redis.hsetnx(redis_key, "registered", "1")  # type: ignore
            if username:
                await self._redis.hset(redis_key, "username", username)  # type: ignore
        except RedisError as e:
            raise BackendOperationError(f"Failed to ensure user: {e}") from e

    async def is_registered(self, user_id: int) -> bool:
        """Check if user is registered."""
        try:
            redis_key = _k(self._prefix, "user", str(user_id))
            result = await self._redis.hexists(redis_key, "registered")  # type: ignore
            return bool(result)  # type: ignore
        except RedisError as e:
            raise BackendOperationError(f"Failed to check registration: {e}") from e

    async def register_user(self, user_id: int, **kwargs: Any) -> None:
        """Register a user with optional data."""
        try:
            redis_key = _k(self._prefix, "user", str(user_id))
            # Set user_id and timestamp
            await self._redis.hset(redis_key, "user_id", str(user_id))  # type: ignore
            await self._redis.hset(redis_key, "registered_at", str(time.time()))  # type: ignore
            # Set additional fields
            for key, value in kwargs.items():
                await self._redis.hset(redis_key, key, str(value))  # type: ignore
        except RedisError as e:
            raise BackendOperationError(f"Failed to register user: {e}") from e

    async def get_user(self, user_id: int) -> dict[str, Any] | None:
        """Get user data by ID."""
        try:
            redis_key = _k(self._prefix, "user", str(user_id))
            data = await self._redis.hgetall(redis_key)  # type: ignore
            if not data:
                return None
            # Convert bytes to strings and parse types
            result: dict[str, Any] = {}
            for key, value in data.items():  # type: ignore
                key_str = key.decode() if isinstance(key, bytes) else str(key)  # type: ignore
                value_str = value.decode() if isinstance(value, bytes) else str(value)  # type: ignore
                # Try to parse as int/float, otherwise keep as string
                if value_str.isdigit():
                    result[key_str] = int(value_str)
                elif value_str.replace(".", "").isdigit():
                    result[key_str] = float(value_str)
                else:
                    result[key_str] = value_str
            return result
        except RedisError as e:
            raise BackendOperationError(f"Failed to get user: {e}") from e
