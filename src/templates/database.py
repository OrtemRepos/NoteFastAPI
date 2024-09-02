import datetime

from sqlalchemy import text

from config import PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_DATABASE
from typing import AsyncGenerator, Annotated
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import mapped_column

DATABASE_URL = (
    f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
)

id_primary = Annotated[int, mapped_column(primary_key=True)]
create_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now()"))]
update_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now()"))]
str_255 = Annotated[str, 255]
str_50 = Annotated[str, 50]


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
