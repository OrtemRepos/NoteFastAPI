from sqlalchemy.orm import mapper, Mapped, mapped_column
from  sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from src.templates.database import id_primary, str_50, str_255, Base, create_at, update_at

from src.schema.note import NoteCreate, NoteRead
from src.model.model import Note



def model_to_dict(model: NoteCreate) -> dict:
    return model.model_dump()


def row_to_model(row: dict) -> NoteCreate:
    title, content, author_id = row
    return Model(title=title, content=content, author_id=author_id)


async def get_one(session: AsyncSession, id: int, id_author: int) -> Model | None:
    result = await session.execute(
        select(note_tabel).where(
            note_tabel.c.id == id, note_tabel.c.author_id == id_author
        )
    )
    return row_to_model(result.scalar())


def get_all(session: AsyncSession, id_author: int) -> list[Model]:
    result = session.execute(
        select(note_tabel).where(note_tabel.c.author_id == id_author)
    )
    return [row_to_model(row) for row in result]


def create(session: AsyncSession, model: Model) -> Model | None:
    if not model or model.author_id is None:
        return
    session.add(model)
    return get_one(session, model.id, model.author_id)
