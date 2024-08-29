from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(Text())
    create_at = Column(TIMESTAMP, default=datetime.utcnow)
    update_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
