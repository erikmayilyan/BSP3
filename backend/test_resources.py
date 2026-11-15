from backend import paths
from backend.agents.prompt_safety_agent import load_dataset


def test_resource_paths_are_anchored_to_the_project():
  assert paths.DATASET_PATH == paths.PROJECT_ROOT / "data" / "requests.csv"
  assert paths.MODEL_PATH == paths.BACKEND_DIR / "ml" / "prompt_safety_model.joblib"


def test_dataset_and_model_exist_on_disk():
  assert paths.DATASET_PATH.is_file()
  assert paths.MODEL_PATH.is_file()


def test_dataset_loads_from_the_safety_agent():
  prompts, labels = load_dataset()

  assert len(prompts) == len(labels) == 1132
  assert set(labels) == {0, 1}
  assert all(isinstance(prompt, str) and prompt for prompt in prompts)
