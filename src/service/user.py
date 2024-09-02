from data import user as data
from auth.schemas import UserCreate, UserRead


async def create_user(user: UserCreate) -> UserRead | None:
    return await data.create_user(user)


async def get_user_by_email(email: str) -> UserRead | None:
    return await data.get_one_by_email(email)


async def get_user(id: int) -> UserRead | None:
    return await data.get_one(id)


async def get_users() -> list[UserRead | None]:
    return await data.get_all()


async def delete_user(user_id: int) -> bool | None:
    return await data.delete_user(user_id)
