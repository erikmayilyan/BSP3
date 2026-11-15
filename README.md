# BSP3
Bachelor Semester Project 3 — multi-agent AI chat for University of Luxembourg students

## Structure

- `backend/` — FastAPI app and orchestrator (`backend/__main__.py`, `backend/orchestrator.py`)
- `backend/agents/` — prompt safety, request analysis, response generation
- `backend/ml/` — training script and saved prompt safety model
- `backend/paths.py` — single source of truth for every resource path
- `data/requests.csv` — labeled prompt dataset
- `frontend/` — React + Vite page

## Run the backend

From the repository root:

```bash
python -m backend
```

The API listens on http://127.0.0.1:8000. The frontend (Vite, port 5173) posts to `/chat`.

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

## Train the prompt safety model

```bash
python -m backend.ml.train_model
```

## Run the tests

```bash
python3 -m pytest backend -q
```

Tests run from the repository root. They check package imports, resource
paths, dataset loading, the `/chat` API, and the dataset accuracy floor.
