from src.schema.note import NoteCreate, NoteRead
from src.templates.database import async_session_maker
from src.model.model import Note

from sqlalchemy import select

def model_to_dict(model: NoteCreate) -> dict:
    return model.model_dump()


def orm_to_model(orm: Note) -> NoteRead:
    return NoteRead.model_validate(orm)

async def get_one(id_note: int, user_id: int) -> NoteRead:
    async with async_session_maker() as session:
        note = await session.get(Note, id_note).filter_by(author_id=user_id).scalar().first()
        return orm_to_model(note)

async def get_all(user_id: int) -> list[NoteRead]:
    async with async_session_maker() as session:
        notes = await session.execute(select(Note).where(Note.author_id == user_id))
        return [orm_to_model(note) for note in notes]

async def create_note(note: NoteCreate):
    async  with async_session_maker() as session:
        new_note = Note(title=note.title, content=note.content, author_id=note.author_id)
        session.add(new_note)
        await session.commit()
        return model_to_dict(new_note)