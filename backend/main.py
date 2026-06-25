from fastapi import FastAPI
from pydantic import BaseModel

from services.ollama_service import generate_response
from core.config import settings
from database.connection import engine
from database.base import Base
import models.conversation
import models.message

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

class ChatRequest(BaseModel):
    conversation_id:int
    message: str

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "online"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    answer = generate_response(
        request.message
    )

    return {
        "response": answer
    }