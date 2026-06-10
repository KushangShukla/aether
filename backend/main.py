from fastapi import FastAPI
from pydantic import BaseModel

from services.ollama_service import generate_response

app = FastAPI(
    title="AETHER",
    version="0.1"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "name": "AETHER",
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