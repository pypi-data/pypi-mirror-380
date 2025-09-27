import os
from pathlib import Path
from typing import AsyncGenerator, Generator
from unittest.mock import patch

import pytest
import pytest_asyncio
from ab_core.database.databases import Database
from ab_core.database.databases.sqlalchemy import AsyncSession, Session
from ab_core.database.session_context import db_session_async_cm, db_session_sync_cm
from ab_core.dependency import Load


@pytest.fixture
def tmp_database_sync(tmp_path: Path) -> Generator[Database, None, None]:
    tmp_db_path = tmp_path / "db.sqlite"
    tmp_db_url = f"sqlite:///{tmp_db_path.as_posix()}"

    with patch.dict(
        os.environ,
        {
            "DATABASE_TYPE": "SQL_ALCHEMY",
            "DATABASE_SQL_ALCHEMY_URL": tmp_db_url,
        },
        clear=False,
    ):
        database: Database = Load(Database)
        database.sync_upgrade_db()
        yield database


@pytest_asyncio.fixture
async def tmp_database_async(tmp_path: Path) -> AsyncGenerator[Database, None]:
    tmp_db_path = tmp_path / "db.sqlite"
    tmp_db_url = f"sqlite+aiosqlite:///{tmp_db_path.as_posix()}"

    with patch.dict(
        os.environ,
        {
            "DATABASE_TYPE": "SQL_ALCHEMY",
            "DATABASE_SQL_ALCHEMY_URL": tmp_db_url,
        },
        clear=False,
    ):
        database: Database = Load(Database)
        await database.async_upgrade_db()
        yield database


@pytest.fixture
def tmp_database_sync_session(tmp_database_sync: Database) -> Generator[Session, None, None]:
    with db_session_sync_cm(tmp_database_sync) as session:
        yield session


@pytest_asyncio.fixture
async def tmp_database_async_session(
    tmp_database_async: Database,
) -> AsyncGenerator[AsyncSession, None]:
    async with db_session_async_cm(tmp_database_async) as session:
        yield session
