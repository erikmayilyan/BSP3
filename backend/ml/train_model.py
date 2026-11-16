import csv
import joblib
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_PATH = PROJECT_ROOT / "data" / "requests.csv"
MODEL_PATH = Path(__file__).resolve().parent / "prompt_safety_model.joblib"

def load_dataset():
  prompts = []
  labels = []

  with open(DATASET_PATH, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
      prompts.append(row["prompt"])
      labels.append(int(row["label"]))

  return prompts, labels

def train_model():
  prompts, labels = load_dataset()

  X_train, X_test, y_train, y_test = train_test_split(
    prompts,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels,
  )

  model = Pipeline([
    ("tfidf", TfidfVectorizer(
      ngram_range=(1, 2),
      min_df=2,
      max_features=100000,
    )),
    ("classifier", LogisticRegression(max_iter=1000)),
  ])

  model.fit(X_train, y_train)

  predictions = model.predict(X_test)

  print("\nClassification report:")
  print(classification_report(
    y_test,
    predictions,
    labels=[0, 1],
    target_names=["Safe (0)", "Unsafe (1)"],
    zero_division=0,
  ))

  print("Confusion matrix:")
  print(confusion_matrix(y_test, predictions, labels=[0, 1]))

  joblib.dump(model, MODEL_PATH)

  print(f"\nModel saved to: {MODEL_PATH}")

if __name__ == "__main__":
  train_model()
