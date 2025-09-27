import os
from pathlib import Path
from typing import AsyncGenerator, Generator
from unittest.mock import patch

import pytest
import pytest_asyncio
from ab_core.cache.caches import Cache
from ab_core.cache.caches.base import BaseSessionAsync, BaseSessionSync
from ab_core.cache.session_context import cache_session_async_cm, cache_session_sync_cm
from ab_core.dependency import Load


@pytest.fixture
def tmp_cache_sync() -> Generator[Cache, None, None]:
    with patch.dict(
        os.environ,
        {
            "CACHE_TYPE": "INMEMORY",
        },
        clear=False,
    ):
        cache: Cache = Load(Cache)
        yield cache


@pytest_asyncio.fixture
async def tmp_cache_async(tmp_path: Path) -> AsyncGenerator[Cache, None]:
    with patch.dict(
        os.environ,
        {
            "CACHE_TYPE": "INMEMORY",
        },
        clear=False,
    ):
        cache: Cache = Load(Cache)
        yield cache


@pytest.fixture
def tmp_cache_sync_session(tmp_cache_sync: Cache) -> Generator[BaseSessionAsync, None, None]:
    with cache_session_sync_cm(tmp_cache_sync) as session:
        yield session


@pytest_asyncio.fixture
async def tmp_cache_async_session(
    tmp_cache_async: Cache,
) -> AsyncGenerator[BaseSessionSync, None]:
    async with cache_session_async_cm(tmp_cache_async) as session:
        yield session
