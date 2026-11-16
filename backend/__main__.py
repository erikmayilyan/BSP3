from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import process_request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
  ],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class ChatRequest(BaseModel):
  message: str

@app.get("/")
def home():
  return {"message" : "Backend is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
  response = process_request(request.message)
  return {"response" : response}
