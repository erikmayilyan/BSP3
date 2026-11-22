import csv
from pathlib import Path
from agents.prompt_safety_agent import check_prompt

DATASET_PATH = Path(__file__).resolve().parents[1] / "data" / "unilu_safety_eval.csv"

def load_dataset():
  with open(DATASET_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    return list(reader)

def evaluate_dataset(dataset):
  results = []

  for row in dataset:
    prompt = row["prompt"]
    expected = row["label"]

    safe, reason = check_prompt(prompt)

    predicted = "safe" if safe else "unsafe"

    results.append({
      "prompt": prompt,
      "expected": expected,
      "predicted": predicted,
      "correct": expected == predicted,
      "reason": reason
    })
  
  return results

def calculate_metrics(results):
  total = len(results)

  correct = sum(1 for row in results if row["correct"])

  false_rejections = sum(
    1 for row in results
      if row["expected"] == "safe" and row["predicted"] == "unsafe"
  )

  missed_unsafe = sum(
    1 for row in results
    if row["expected"] == "unsafe" and row["predicted"] == "safe"
  )

  accuracy = (correct / total) * 100 if total > 0 else 0

  print("\nEvaluation Results")
  print("------------------")
  print(f"Total prompts: {total}")
  print(f"Correct predictions: {correct}")
  print(f"Accuracy: {accuracy:.2f}%")
  print(f"False rejections: {false_rejections}")
  print(f"Missed unsafe prompts: {missed_unsafe}")

if __name__ == "__main__":
  dataset = load_dataset()
  results = evaluate_dataset(dataset)
  print("Evaluated prompts: ", len(results))
  calculate_metrics(results)