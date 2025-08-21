import os, sys, pathlib

# Ensure repo root on sys.path so 'services' imports reliably
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Use stub model in tests (no MLflow needed)
os.environ["SKIP_MODEL_LOAD"] = "1"

from fastapi.testclient import TestClient
from services.api.app import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_predict_returns_species():
    r = client.post("/predict", json={"features": [38.5, 18.5, 190, 4000]})
    assert r.status_code == 200
    body = r.json()
    assert "species" in body and isinstance(body["species"], str)