from data import user as data
from auth.schemas import UserCreate, UserRead


async def get_user(user_id: int) -> UserRead:
    return await data.get_one(user_id)


def get_users() -> list[UserRead]:
    return data.get_all()


async def create_user(user: UserCreate) -> None:
    return await data.create_user(user)
