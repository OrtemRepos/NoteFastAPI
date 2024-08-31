from fastapi_users import schemas
from datetime import datetime
from pydantic import Field


class UserRead(schemas.BaseUser[int]):
    username: str
    register_at: datetime = Field(default=datetime.utcnow())


class UserCreate(schemas.BaseUserCreate):
    username: str
    register_at: datetime = Field(default=datetime.utcnow())


class UserUpdate(schemas.BaseUserUpdate):
    username: str
