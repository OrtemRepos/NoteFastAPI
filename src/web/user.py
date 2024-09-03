from fastapi import APIRouter, Depends
from service import user as service
from auth.schemas import UserRead, UserCreate
from auth.auth import current_super_user

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=list[UserRead])
async def get_users():
    return await service.get_users()


@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, current_user: UserRead = Depends(current_super_user)):
    return await service.create_user(user)
