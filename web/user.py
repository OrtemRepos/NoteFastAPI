from fastapi import APIRouter
from service import user as service
from model.user import UserRead, UserCreate

router = APIRouter(prefix="/user")


@router.get("/", response_model=UserRead)
def get_all():
    return service.get_users()


@router.get("/{id}", response_model=UserRead)
async def get_user(id: int):
    return service.get_user(id)


@router.post("/create", response_model=UserRead)
async def create_user(user: UserCreate):
    return service.create_user(user)
