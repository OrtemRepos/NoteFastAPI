from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict, StringConstraints
from typing_extensions import Annotated


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: Annotated[EmailStr, StringConstraints(min_length=5, max_length=50)]
    username: Annotated[str, StringConstraints(min_length=5, max_length=50)]
    register_at: datetime


class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: Annotated[EmailStr, StringConstraints(min_length=5, max_length=50)]
    username: Annotated[str, StringConstraints(min_length=5, max_length=50)]
    register_at: datetime = Field(default=datetime.utcnow())
    password: Annotated[str, StringConstraints(min_length=5, max_length=20)]
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    is_verified: bool = Field(default=False)


