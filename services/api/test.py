import requests

predict_endpoint = "http://localhost:8000/predict"
health_endpoint = "http://localhost:8000/health"

payload = [{
    "bill_length_mm": 48.7,
    "bill_depth_mm": 18.6,
    "flipper_length_mm": 195,
    "body_mass_g": 3800,
    "island": "Dream",
    "sex": "female"
}]

# Test prediction endpoint
res = requests.post(predict_endpoint, json=payload)
print(res.json())

# Test health endpoint
res = requests.get(health_endpoint)
print(res.json())