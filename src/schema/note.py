from datetime import datetime
from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str
    content: str
    create_at: datetime
    update_at: datetime
    author_id: int


class NoteRead(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    create_at: datetime
    update_at: datetime
