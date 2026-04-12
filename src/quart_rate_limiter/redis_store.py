from datetime import datetime
from typing import Any

from redis import asyncio as aioredis

from .store import RateLimiterStoreABC


class RedisStore(RateLimiterStoreABC):
    """An redis backed store of rate limits.

    Arguments:
        address: The address of the redis instance.
        kwargs: Any keyword arguments to pass to the redis client on
            creation, see the redis documentation.
    """

    def __init__(self, address: str, **kwargs: Any) -> None:
        self._redis: aioredis.Redis | None = None
        self._redis_arguments = (address, kwargs)

    async def before_serving(self) -> None:
        pass

    async def get(self, key: str, default: datetime) -> datetime:
        pass

    async def set(self, key: str, tat: datetime) -> None:
        pass

    async def after_serving(self) -> None:
        pass
