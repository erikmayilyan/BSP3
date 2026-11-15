import os
import subprocess
import sys
from pathlib import Path

import backend

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_backend_is_a_regular_package():
  assert backend.__file__ is not None


def test_public_api_imports_from_any_directory(tmp_path):
  env = {**os.environ, "PYTHONPATH": str(PROJECT_ROOT)}
  result = subprocess.run(
    [sys.executable, "-c", "import backend.orchestrator"],
    cwd=tmp_path,
    env=env,
    capture_output=True,
    text=True,
  )

  assert result.returncode == 0, result.stderr
