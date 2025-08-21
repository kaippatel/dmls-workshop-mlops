import requests

predict_endpoint = "http://localhost:8000/predict"
data = [{
    "bill_length_mm": 39.1,
    "bill_depth_mm": 18.7,
    "flipper_length_mm": 181,
    "body_mass_g": 3750,
    "island": "Torgersen",
    "sex": "male"
}]

# Test prediction API
res = requests.post(predict_endpoint, json=data)
print(res.json())