from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parents[1] / "ml" / "prompt_safety_model.joblib"
model = joblib.load(MODEL_PATH)

def check_prompt(user_request: str) -> tuple[bool, str]:
  prediction = int(model.predict([user_request])[0])

  if prediction == 1:
    return False, "The prompt was classified as unsafe by the ML model."

  return True, "The prompt was classified as safe by the ML model."

  request = user_request.lower()

  for phrase in blocked_phrases:
    if phrase in request:
      return False

  return True
