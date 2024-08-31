import asyncio
import contextlib

from sqlalchemy import select
from src.templates.database import async_session_maker

from src.auth.database import get_async_session, get_user_db
from fastapi_users.exceptions import UserAlreadyExists
from src.auth.manager import get_user_manager
from src.auth.schemas import UserCreate, UserRead
from src.auth.database import User


def orm_to_user(orm_user) -> UserRead:
    return UserRead.model_validate(orm_user)


def user_to_dict(user: UserCreate) -> dict:
    return user.model_dump()


async def get_one(id_user: int) -> UserRead:
    state = select(User).where(User.id == id_user)
    async with async_session_maker() as session:
        result = await session.execute(state)
    return orm_to_user(result.scalars().first())


async def get_all() -> list[UserRead]:
    state = select(User)
    async with async_session_maker() as session:
        result = await session.execute(state)
    return [orm_to_user(row) for row in result.scalars().all()]


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(user: UserCreate):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(user)
                    print(f"User created {user}")
    except UserAlreadyExists:
        print(f"User {user.email} already exists")
