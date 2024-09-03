from urllib import response

from tomlkit import boolean
from model.model import User
from schema.note import NoteCreate, NoteRead, NoteUpdate
from service import note as service
from auth.auth import current_active_user
from fastapi import APIRouter, Depends, status, Response

router = APIRouter(prefix="/note", tags=["note"])



@router.post("/",
            response_model=NoteRead,
            status_code=status.HTTP_201_CREATED,
            name="note:create",
            responses={status.HTTP_201_CREATED: {"model": NoteRead}}
            )
async def create_note(
    note: NoteCreate,
    user: User = Depends(current_active_user),
):
    return await service.create_note(note, author_id = user.id)

@router.get("/",
           response_model=list[NoteRead],
           status_code=status.HTTP_200_OK,
           name="note:get_all_notes_for_current_user",
           responses={status.HTTP_401_UNAUTHORIZED: {"Disription": "Not authorized"}}
           )
async def get_notes(user: User = Depends(current_active_user)):
    return await service.get_notes(user.id)

@router.get("/{note_id}",
           status_code=status.HTTP_200_OK,
           name="note:get_note_for_current_user",
           responses={status.HTTP_401_UNAUTHORIZED: {"Disription": "Not authorized"}})
async def get_note(note_id: int, user: User = Depends(current_active_user)) -> NoteRead:
    return await service.get_note(note_id, user.id)


@router.put("/{note_id}",
           status_code=status.HTTP_200_OK,
           name="note:update_note_for_current_user",
           responses={status.HTTP_401_UNAUTHORIZED: {"Disription": "Not authorized"}})
async def update_note(note_id: int, note: NoteUpdate, user: User = Depends(current_active_user)) -> bool:
    return await service.update_note(note_id, note, user.id)

@router.delete("/{note_id}",
              status_code=status.HTTP_200_OK,
              name="note:delete_note_for_current_user",
              responses={status.HTTP_401_UNAUTHORIZED: {"Disription": "Not authorized"}})
async def delete_note(note_id: int, user: User = Depends(current_active_user)) -> bool:
    return await service.delete_note(note_id, user.id)