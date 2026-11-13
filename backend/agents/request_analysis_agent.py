def analyze_request(user_request: str) -> str:
  request = user_request.lower()

  if "erasmus" in request:
    return "The student is asking about the Erasmus programme."

  if "grade" in request or "grading" in request or "mark" in request:
    return "The student is asking about grading."

  return "The student is asking about an academic topic or another subject."
