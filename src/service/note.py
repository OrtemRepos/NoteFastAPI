from data import note as data
from schema.note import NoteCreate, NoteRead

async def get_one(note_id: int, author_id: int) -> NoteRead:
    return await data.get_one(note_id, author_id)


async def get_all(author_id: int) -> list[NoteRead]:
    return await data.get_all(author_id)

async def create_note(note: NoteCreate) -> NoteRead:
    return await data.create_note(note)
