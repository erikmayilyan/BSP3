def generate_response(user_request: str, analysis: str) -> str:
  if "Erasmus" in analysis:
    return (
      "To apply for the Erasmus programme, start by checking "
      "your university's eligibility requirements, available "
      "partner universities, and application deadlines. "
      "You can also contact the international office for guidance."
    )
  
  if "grading" in analysis:
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
  