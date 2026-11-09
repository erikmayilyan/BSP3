from agents.prompt_safety_agent import check_prompt

def process_request(user_request: str) -> str:
  is_safe = check_prompt(user_request)

  if not is_safe:
    return "Your request was rejected for safety reasons."

  return f"Received your request: {user_request}"
  