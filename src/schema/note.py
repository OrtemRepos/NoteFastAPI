import asyncio
from datetime import datetime
from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    author_id: int
    create_at: datetime | None
    update_at: datetime | None


class NoteRead(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    create_at: datetime
    update_at: datetime | None


class NoteUpdate(NoteRead):
    update_at: datetime | None
