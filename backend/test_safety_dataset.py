import csv
from pathlib import Path
from agents.prompt_safety_agent import check_prompt

DATASET_PATH = Path(__file__).resolve().parents[1] / "data" / "requests.csv"

def test_safety_dataset():
  safe_passed = 0
  safe_rejected = 0
  unsafe_rejected = 0
  unsafe_passed = 0

  with open(DATASET_PATH, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
      prompt = row["prompt"]
      expected_label = int(row["label"])

      is_safe, reason = check_prompt(prompt)

      if expected_label == 0:
        if is_safe:
          safe_passed += 1
        else:
          safe_rejected += 1

      elif expected_label == 1:
        if not is_safe:
          unsafe_rejected += 1
        else:
          unsafe_passed += 1

  total = safe_passed + safe_rejected + unsafe_rejected + unsafe_passed
  correct = safe_passed + unsafe_rejected

  print("\nPrompt Safety Agent - Dataset Evaluation")
  print("----------------------------------------")
  print(f"Total prompts: {total}")
  print(f"Safe prompts passed: {safe_passed}")
  print(f"Safe prompts rejected: {safe_rejected}")
  print(f"Unsafe prompts rejected: {unsafe_rejected}")
  print(f"Unsafe prompts passed: {unsafe_passed}")
  print(f"Accuracy: {correct / total * 100:.2f}%")

if __name__ == "__main__":
  test_safety_dataset()
