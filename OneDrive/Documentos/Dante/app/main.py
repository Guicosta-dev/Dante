from fastapi import FastAPI
from pydantic import BaseModel

from app.chatbot import identificar_intencao

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "DANTE AI está online"}


@app.post("/chat")
def chat(request: ChatRequest):

    intencao = identificar_intencao(request.message)

    return {
        "message": request.message,
        "intencao": intencao
    }