from data import note as data
from schema.note import NoteCreate, NoteRead, NoteUpdate


async def create_note(note: NoteCreate) -> NoteRead:
    return await data.create_note(note)


async def get_note(note_id: int, author_id: int) -> NoteRead:
    return await data.get_one(note_id, author_id)


async def get_notes(author_id: int) -> list[NoteRead]:
    return await data.get_all(author_id)


async def delete_note(note_id: int, author_id: int) -> NoteRead:
    return await data.delete_note(note_id, author_id)


async def update_note(note: NoteUpdate) -> NoteRead:
    return await data.update_note(note)
