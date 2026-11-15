import csv

import joblib

from backend.paths import DATASET_PATH, MODEL_PATH

_model = None


def load_dataset() -> tuple[list[str], list[int]]:
  prompts = []
  labels = []

  with open(DATASET_PATH, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
      prompts.append(row["prompt"])
      labels.append(int(row["label"]))

  return prompts, labels


def load_model():
  global _model

  if _model is None:
    _model = joblib.load(MODEL_PATH)

  return _model


def check_prompt(user_request: str) -> tuple[bool, str]:
  prediction = int(load_model().predict([user_request])[0])

  if prediction == 1:
    return False, "The prompt was classified as unsafe by the ML model."

  return True, "The prompt was classified as safe by the ML model."
