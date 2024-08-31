from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.orm import mapped_column, mapper, Mapped
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.model import User
from src.templates.database import get_async_session, id_primary, create_at, update_at, str_50, str_255


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
