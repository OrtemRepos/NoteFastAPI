from service import note as service

from fastapi import APIRouter

route = APIRouter(prefix='/note', tags=['Note'])

@route.get('/{id_note}', response_model=service.NoteRead)
async def get_note(id_note: int, depends=service.get_current_user):
    return await service.get_note(id_note)