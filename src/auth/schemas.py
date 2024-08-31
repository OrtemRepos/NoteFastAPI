from fastapi_users import schemas
import datetime
from pydantic import Field


class UserRead(schemas.BaseUser[int]):
    username: str
    register_at: datetime.datetime
    update_at: datetime.datetime


class UserCreate(schemas.BaseUserCreate):
    username: str
    register_at: datetime.datetime = Field(default=datetime.datetime.now(datetime.UTC))


class UserUpdate(schemas.BaseUserUpdate):
    username: str
