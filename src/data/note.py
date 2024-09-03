from tomlkit import boolean
from schema.note import NoteCreate, NoteRead, NoteUpdate
from model.model import Note
from templates.database import async_session_maker

from sqlalchemy import Boolean, delete, select, true, update

def orm_to_note(orm_obj: Note) -> NoteRead:
    return NoteRead.model_validate(orm_obj)


def note_to_dict(note: NoteCreate | NoteRead | NoteUpdate) -> dict:
    return note.model_dump()


async def create_note(note: NoteCreate, author_id: int) -> NoteRead:
    title, content = note.title, note.content
    note_row = Note(title=title, content=content, author_id=author_id)
    async with async_session_maker() as session:
        session.add(note_row)
        await session.commit()
        await session.refresh(note_row)
        return NoteRead.model_validate(note_row)


async def get_all(author_id: int) -> list[NoteRead]:
    async with async_session_maker() as session:
        result = await session.execute(select(Note).where(Note.author_id == author_id))
        return [NoteRead.model_validate(row) for row in result.scalars().all()]


async def get_one(note_id: int, author_id: int) -> NoteRead:
    async with async_session_maker() as session:
        result = await session.execute(
            select(Note).where(Note.id == note_id, Note.author_id == author_id)
        )
        return NoteRead.model_validate(result.scalars().first())


async def update_note(note_id : int, note: NoteUpdate, author_id: int) -> bool:
    state = update(Note).where(Note.id == note_id, Note.author_id == author_id)
    async with async_session_maker() as session:
        await session.execute(state, note_to_dict(note))
        await session.commit()
        return True

async def delete_note(note_id: int, author_id: int) -> bool:
    state = delete(Note).where(Note.id == note_id, Note.author_id == author_id)
    async with async_session_maker() as session:
        await session.execute(state)
        await session.commit()
    return True
