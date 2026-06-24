from sqlalchemy import Column, Integer, Text, String, ForeignKey

from database.base import Base

class Message(Base):
    __tablename__="messages"

    id=Column(Integer,primary_key=True,index=True)

    conversation_id=Column(Integer,ForeignKey("conversations.id"))

    role=Column(String)

    content=Column(Text)