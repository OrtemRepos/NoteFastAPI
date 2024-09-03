from datetime import datetime
from pydantic import BaseModel, ConfigDict


class NoteCreate(BaseModel):
    title: str
    content: str
    
    model_config = ConfigDict(from_attributes=True)


class NoteRead(NoteCreate):
    id: int
    author_id: int
    title: str
    content: str
    create_at: datetime
    update_at: datetime | None


class NoteUpdate(NoteCreate):
    update_at: datetime | None 
