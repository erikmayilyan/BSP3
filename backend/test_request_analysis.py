import csv
from pathlib import Path
from agents.request_analysis_agent import analyze_request

DATASET_PATH = Path(__file__).resolve().parents[1] / "data" / "category_questions.csv"

def test_category_questions():
  with open(DATASET_PATH, newline="", encoding="utf-8") as file:
    rows = csv.DictReader(file)

    for row in rows:
      question = row["question"]
      expected = set(row["expected"].split("|"))

      result = analyze_request(question)

      assert set(result["categories"]) == expected, (
        f"\nQuestion: {question}"
        f"\nExpected: {expected}"
        f"\nReceived: {result['categories']}"
      )

def test_other_category():
  result = analyze_request("What is the weather tomorrow?")
  assert result["categories"] == ["other"]