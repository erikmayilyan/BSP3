from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.orchestrator import process_request

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
  return {"message": "Backend is running!"}


@app.post("/chat")
def chat(request: ChatRequest):
  response = process_request(request.message)
  return {"response": response}


if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="127.0.0.1", port=8000)
