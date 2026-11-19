import os
import httpx
from dotenv import load_dotenv
import json
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

provider = os.getenv("LLM_PROVIDER", "ollama").lower()
ollama_model = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
ollama_host = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

openai_api_key = os.getenv("OPENAI_API_KEY")

openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def send_request(url: str, payload: dict, headers: dict = None):
  for attempt in range(2):  
    try:
      response = httpx.post(
        url,
        json=payload,
        headers=headers,
        timeout=60
      )
      response.raise_for_status()
      return response

    except (httpx.RequestError, httpx.HTTPStatusError):
      if attempt == 1:
        raise

def ask_llm(prompt: str, json_mode: bool = False) -> str | dict:
  if provider == "ollama":
    payload = {
      "model": ollama_model,
      "prompt": prompt,
      "stream": False
    }
    if json_mode:
      payload["format"] = "json"
    response = send_request(
      ollama_host + "/api/generate",
      payload
    )
    answer = response.json()["response"]
    if json_mode:
      return json.loads(answer)
    return answer
  elif provider == "openai":
    if not openai_api_key:
      raise ValueError("OPENAI_API_KEY is not configured.")
    payload = {
      "model": openai_model,
      "messages": [
        {
          "role": "user",
          "content": prompt
        }
      ]
    }
    if json_mode:
      payload["response_format"] = { "type": "json_object" }
    response = send_request(
      "https://api.openai.com/v1/chat/completions",
      payload,
      headers={
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
      }
    )
    answer = response.json()["choices"][0]["message"]["content"]
    if json_mode:
      return json.loads(answer)
    return answer
  else:
    raise ValueError("Invalid LLM provider: " + provider)
