from datetime import datetime
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    TIMESTAMP,
    Boolean,
    select
)
from sqlalchemy.orm import Mapped, mapped_column
from fastapi import Depends
from templates.database import async_session_maker, Base
from model.user import UserCreate, UserRead
from error import MissingException, DuplicateException

import asyncio


class User(Base):
    __tablename__ = "user"


    ID: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str]
    register_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)

    # email = Column(String, nullable=False)
    # username = Column(String, nullable=False)
    # register_at = Column(type_=TIMESTAMP(timezone=True), default=datetime.utcnow)
    # password = Column(String(length=1024), nullable=False)
    # is_active = Column(Boolean, default=True, nullable=False)
    # is_superuser = Column(Boolean, default=False, nullable=False)
    # is_verified = Column(Boolean, default=False, nullable=False)




def orm_to_user(orm_user) -> UserRead:
    return UserRead.model_validate(orm_user)


def user_to_dict(user: UserCreate) -> dict:
    return user.model_dump()


async def get_one(
    id: int) -> UserRead:
    state = select(User).where(User.id == id)
    async with async_session_maker() as session:
        result = await session.execute(state)
    return orm_to_user(result.scalars().first())

async def get_all() -> list[UserRead]:
    state = select(User)
    async with async_session_maker() as session:
        result = await session.execute(state)
    return [orm_to_user(row) for row in result.scalars().all()]

# if __name__ == "__main__":
#     sample = UserCreate(username="username", email="email@mail.ru", password="password")
#     user = User(**user_to_dict(sample))
#     print(asyncio.run(create(user)))