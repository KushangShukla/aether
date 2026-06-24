from fastapi import FastAPI
from pydantic import BaseModel

from services.ollama_service import generate_response
from core.config import Settings

settings=Settings.settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


class ChatRequest(BaseModel):
    message: str


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