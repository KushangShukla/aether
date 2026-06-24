from sqlalchemy.orm import Session

from models.conversation import Conversation
from models.message import Message

def create_conversation(db:Session):
    conversation=Conversation()

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation

def save_message(
        db:Session,
        conversation_id:int,
        role:str,
        content:str
):
    message=Message(
        conversation_id=conversation_id,
        role=role,
        content=content
    )
    db.add(message)
    db.commit()

    return message