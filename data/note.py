from datetime import datetime


from sqlalchemy import MetaData, select, ForeignKey, Table, Column, Integer, String, TIMESTAMP, Text
from sqlalchemy.ext.asyncio import AsyncSession
from templates.database import get_async_session


from user import user_tabel
from model.note import Note as Model


metadata = MetaData()

note_tabel = Table(
    'note',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('title', String(50), nullable=False),
    Column('content', Text()),
    Column('create_at', TIMESTAMP, default=datetime.utcnow),
    Column('update_at', TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow),
    Column('author_id', Integer, ForeignKey(user_tabel.c.id))
)

def model_to_dict(model: Model) -> dict:
    return model.model_dump()

def row_to_model(row: dict) -> Model:
    title, content, author_id = row
    return Model(title=title, content=content, author_id=author_id)

async def get_one(session: AsyncSession, id: int, id_author: int) -> Model | None:
    result = await session.execute(select(note_tabel).where(note_tabel.c.id == id, note_tabel.c.author_id == id_author))
    return row_to_model(result.scalar())

def get_all(session: AsyncSession, id_author: int) -> list[Model]:
    result = session.execute(select(note_tabel).where(note_tabel.c.author_id == id_author))
    return [row_to_model(row) for row in result]

def create(session: AsyncSession, model: Model) -> Model | None:
    if not model or model.author_id is None:
        return
    session.add(model)
    return get_one(session, model.id, model.author_id)


    

