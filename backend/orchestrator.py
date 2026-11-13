from agents.prompt_safety_agent import check_prompt
from agents.request_analysis_agent import analyze_request

def process_request(user_request: str) -> str:
  is_safe, reason = check_prompt(user_request)

  if not is_safe:
    return f"Your request was rejected for safety reasons. Reason: {reason}"

  return analyze_request(user_request)
