from fastapi.testclient import TestClient
from app import app  

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    print("Health:", resp.json())

def test_predict_single():
    payload = {
        "pclass": 1,
        "sex": "female",
        "age": 38,
        "sibsp": 1,
        "parch": 0,
        "fare": 71.2833,
        "embarked": "C",
        "class": "First",       
        "who": "woman",
        "adult_male": False,
        "deck": "C",
        "embark_town": "Cherbourg",
        "alone": False
    }

    resp = client.post("/predict", json=payload)
    assert resp.status_code == 200
    print("Prediction:", resp.json())

if __name__ == "__main__":
    test_health()
    test_predict_single()