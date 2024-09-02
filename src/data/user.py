import contextlib

from fastapi_users.exceptions import UserAlreadyExists
from sqlalchemy import select

from auth.database import User
from auth.database import get_async_session, get_user_db
from auth.manager import get_user_manager
from auth.schemas import UserCreate, UserRead
from templates.database import async_session_maker


def orm_to_user(orm_user) -> UserRead:
    return UserRead.model_validate(orm_user)


def user_to_dict(user: UserCreate) -> dict:
    return user.model_dump()


async def get_one(id_user: int) -> UserRead:
    async with async_session_maker() as session:
        result = await session.get_one(User, id=id_user)
    return orm_to_user(result)


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

