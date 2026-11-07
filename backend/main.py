from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import process_request

app = FastAPI()

class ChatRequest(BaseModel):
  message: str

@app.get("/")
def home():
  return {"message" : "Backend is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
  response = process_request(request.message)
  return {"response" : response}
