import asyncio
import pytest
from data import user as data
from auth.schemas import UserCreate, UserRead
from fastapi_users.exceptions import UserAlreadyExists
