from agents.prompt_safety_agent import check_prompt

def process_request(user_request: str) -> str:
  is_safe, reason = check_prompt(user_request)

  if not is_safe:
    return f"Your request was rejected for safety reasons. Reason: {reason}"

  return f"Received your request: {user_request}"
