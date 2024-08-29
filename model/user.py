from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    email: str
    username: EmailStr
    register_at: datetime
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool