from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship

from database.base import Base

class Message(Base):
    __tablename__="messages"

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)

    conversation_id:Mapped[int]=mapped_column(ForeignKey("conversations.id"))

    role:Mapped[str]=mapped_column(String(20))

    content:Mapped[str]=mapped_column(Text)

    conversation=relationship("Conversation",back_populates="messages")