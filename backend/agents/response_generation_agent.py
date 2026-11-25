from llm import ask_llm

def fallback_response(user_request: str, categories: list[str]) -> str:
  if "mobility" in categories:
    return (
      "To apply for the Erasmus programme, start by checking "
      "your university's eligibility requirements, available "
      "partner universities, and application deadlines. "
      "You can also contact the international office for guidance."
    )
  
  if "academic" in categories:
    return (
      "To understand the grading system, check your course "
      "syllabus for the assessment criteria, grading scale, "
      "and minimum passing requirements. If something is unclear, "
      "contact your course instructor."
    )

  return (
    f"I can help you with your academic question: {user_request} "
    "Let's break it down step by step."
  )

def build_response_prompt(user_request: str, categories: list[str]) -> str:
  return f"""
  You are an AI assistant for students at the University of Luxembourg.
  Your task is to answer the student's question accurately and clearly.
  
  Relevant categories: {", ".join(categories)}

  Instructions:
  - Keep your answer between 3 and 5 sentences.
  - Be clear, helpful, and easy to understand.
  - Focus on the student's actual question.
  - Do not invent deadlines, fees, names, or university policies.
  - If you do not know a specific detail, say so rather than guessing.
  - Do not claim that uncertain information is confirmed.

  Student's question:
  {user_request}
  """
  
def generate_response(user_request: str, analysis: dict) -> str:
  categories = analysis["categories"]
  
  try:
    answer = ask_llm(
      build_response_prompt(user_request, categories),
      temperature=0.3
    )
    if isinstance(answer, str) and answer.strip():
      return answer.strip()
  except Exception:
    pass
  
  return fallback_response(user_request, categories)
  