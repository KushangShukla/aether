from pydantic import BaseModel

class ChatRequest(BaseModel):
    conversation_id:int
    message:str