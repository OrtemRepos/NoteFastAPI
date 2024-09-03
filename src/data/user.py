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


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(user: UserCreate) -> UserRead | None:
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(user)  # type: ignore
                    print(f"User created {user}")
                    return UserRead.model_validate(user)
    except UserAlreadyExists:
        print(f"User {user.email} alreadyExists")


async def get_all() -> list[UserRead | None]:
    state = select(User)
    async with async_session_maker() as session:
        result = await session.execute(state)
    return [orm_to_user(row) for row in result.scalars().all()]
