from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.orm import mapped_column, mapper, Mapped
from sqlalchemy.ext.asyncio import AsyncSession

from model.model import User
from templates.database import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
