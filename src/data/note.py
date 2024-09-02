from turtle import update
from schema.note import NoteCreate, NoteRead, NoteUpdate
from model.model import Note
from templates.database import async_session_maker

from sqlalchemy import delete, select, update


def orm_to_note(orm_obj: Note) -> NoteRead:
    return NoteRead.model_validate(orm_obj)


def note_to_dict(note: NoteCreate | NoteRead | NoteUpdate) -> dict:
    return note.model_dump()


async def create_note(note: NoteCreate) -> NoteRead:
    async with async_session_maker() as session:
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return NoteRead.model_validate(note)


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


async def update_note(note: NoteUpdate) -> NoteRead:
    state = update(Note)
    async with async_session_maker() as session:
        res = await session.execute(state, note_to_dict(note))
        await session.commit()
        return NoteRead.model_validate(res.scalars().first())


async def delete_note(note_id: int, author_id: int) -> NoteRead:
    state = delete(Note).where(Note.id == note_id, Note.author_id == author_id)
    async with async_session_maker() as session:
        res = await session.execute(state)
        await session.commit()
    return orm_to_note(res.scalars().first())  # type: ignore
