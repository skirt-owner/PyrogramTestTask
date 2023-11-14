from sqlalchemy import URL, MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from bot import config


def get_async_session_maker(engine: AsyncEngine) -> async_sessionmaker:
    """
    Get an asynchronous session maker for a given database engine.

    :param engine: The async engine to bind the session maker to.
    :type engine: AsyncEngine

    :return: An asynchronous session maker object.
    :rtype: async_sessionmaker
    """
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )


def create_database_url() -> URL:
    """
    Create a database URL based on the provided configuration.

    :return: A database URL object.
    :rtype: URL
    """
    return URL.create(
        drivername="postgresql+asyncpg",
        username=config.postgres_username,
        password=config.postgres_password,
        host=config.postgres_host,
        port=config.postgres_port,
        database=config.postgres_database
    )


def create_async_engine(database_url: URL) -> AsyncEngine:
    """
    Create an asynchronous SQLAlchemy engine based on the provided database URL.

    :param database_url: The database URL to connect to.
    :type database_url: URL

    :return: An asynchronous engine object.
    :rtype: AsyncEngine
    """
    return _create_async_engine(
        database_url,
        echo=True
    )


async def init_models(engine: AsyncEngine, metadata: MetaData) -> None:
    """
    Initialize database models by dropping and creating tables.

    :param engine: The async engine used to connect to the database.
    :type engine: AsyncEngine

    :param metadata: The SQLAlchemy metadata object containing the table definitions.
    :type metadata: MetaData
    """
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
