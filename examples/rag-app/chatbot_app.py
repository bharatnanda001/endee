from fastapi import FastAPI
from chatbot import generate_answer

app = FastAPI()

@app.get("/chat")
def chat(q: str):
    answer = generate_answer(q)
    return {"response": answer}
