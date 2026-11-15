"""Single source of truth for every resource path in the backend.

Every path is derived from this file's location, so resources resolve the
same way no matter which directory Python is started from.
"""

from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BACKEND_DIR.parent

DATA_DIR = PROJECT_ROOT / "data"
ML_DIR = BACKEND_DIR / "ml"

DATASET_PATH = DATA_DIR / "requests.csv"
MODEL_PATH = ML_DIR / "prompt_safety_model.joblib"
