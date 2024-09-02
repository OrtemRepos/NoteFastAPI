from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, relationship

from src.templates.database import str_50, id_primary, create_at, update_at, str_255
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[id_primary]
    email: Mapped[str_50]
    username: Mapped[str_255]
    register_at: Mapped[create_at]
    update_at: Mapped[update_at]
    hashed_password: Mapped[str]
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    is_verified: Mapped[bool]

    notes: Mapped[list["Note"]] = relationship("Note", back_populates="author")

class Note(Base):
    __tablename__ = 'note'

    id: Mapped[id_primary]
    title: Mapped[str_50]
    content: Mapped[str]
    create_at: Mapped[create_at]
    update_at: Mapped[update_at]
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))

    author: Mapped["User"] = relationship("User", back_populates="note")
