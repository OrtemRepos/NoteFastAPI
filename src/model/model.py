import datetime
from typing import Annotated
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, text

from templates.database import str_50, id_primary, str_255
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import TIMESTAMP


created_at = Annotated[
    datetime.datetime,
    mapped_column(
        type_=TIMESTAMP(timezone=True), server_default=text("TIMEZONE('utc', now())")
    ),
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        type_=TIMESTAMP(timezone=True),
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=text("TIMEZONE('utc', now())"),
    ),
]


class Base(DeclarativeBase):
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[id_primary]
    email: Mapped[str_50]
    username: Mapped[str_255]
    register_at: Mapped[created_at]
    update_at: Mapped[updated_at]
    hashed_password: Mapped[str]
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    is_verified: Mapped[bool]

    notes: Mapped[list["Note"]] = relationship("Note", back_populates="author")


class Note(Base):
    __tablename__ = "note"

    id: Mapped[id_primary]
    title: Mapped[str_50]
    content: Mapped[str]
    create_at: Mapped[created_at]
    update_at: Mapped[updated_at]
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

    author: Mapped["User"] = relationship("User", back_populates="notes")
