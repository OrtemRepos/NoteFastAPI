import data
import fastapi_users
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from model.model import User
from auth.auth import auth_backend
from schema.note import NoteCreate
from service import note as service

from fastapi import APIRouter, Depends

route = APIRouter(prefix="/note", tags=["Note"])

fastapi_users = FastAPIUsers[User, int](  # type: ignore
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)


@route.get("/{id_note}")
async def get_note(id_note: int, user: User = Depends(current_active_user)):
    return await service.get_note(id_note, user.id)


@route.get("/")
async def get_notes(user: User = Depends(current_active_user)):
    return await service.get_notes(user.id)


@route.post("/")
async def create_note(note: NoteCreate, user: User = Depends(current_active_user)):
    return await service.create_note(note)
