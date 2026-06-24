from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import Mapped,mapped_column,relationship

from datetime import datetime

from database.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    created_at:Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)

    messages=relationship("Message",back_populates="conversation")