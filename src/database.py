from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .config import config

engine = create_async_engine(url=config.DB_URL)
session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)