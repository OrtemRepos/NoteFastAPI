from fastapi_users import schemas
import datetime


class UserRead(schemas.BaseUser[int]):
    username: str
    register_at: datetime.datetime
    update_at: datetime.datetime


class UserCreate(schemas.BaseUserCreate):
    username: str
    register_at: datetime.datetime | None


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    update_at: datetime.datetime | None
