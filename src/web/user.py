from fastapi import APIRouter
from service import user as service
from auth.schemas import UserRead, UserCreate

router = APIRouter(prefix="/user", tags=["test"])


@router.get("/", response_model=list[UserRead])
async def get_users():
    return await service.get_users()


@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate):
    return await service.create_user(user)


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int):
    return await service.get_user(user_id)


@router.get("/", response_model=UserRead)
async def get_user_by_email(email: str):
    return await service.get_user_by_email(email)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return await service.delete_user(user_id)
