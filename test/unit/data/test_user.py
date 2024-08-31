import pytest
from fastapi import Depends
from data import user as data
from model.user import UserRead, UserCreate
from templates.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
def sample():
    return UserCreate(username="username", email="email@mail.ru", password="password")

async def test_get_one(id: int, session: AsyncSession = Depends(get_async_session)):
    


def test_get_one(id: int = 3):
    result = data.get_one(id)
    print(result)
    assert result


test_get_one()


