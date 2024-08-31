from data import user as data


async def get_user(user_id: int):
    return await data.get_one(user_id)


def get_users():
    return data.get_all()


async def create_user(user: data.UserCreate):
    return await data.create(user)
