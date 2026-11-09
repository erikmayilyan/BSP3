def check_prompt(user_request: str) -> bool:
  blocked_phrases = [
    "ignore previous instructions",
    "ignore all instructions",
    "how to make a bomb",
    "how to kill someone",
  ]

  request = user_request.lower()

  for phrase in blocked_phrases:
    if phrase in request:
      return False

  return True
