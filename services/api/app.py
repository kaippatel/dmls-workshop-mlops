from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import mlflow.pyfunc
import mlflow
import pandas as pd
import time 
import os 

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
MODEL_URI = os.getenv("MODEL_URI")
model = mlflow.pyfunc.load_model(MODEL_URI)

app = FastAPI(title="Penguins Classifier API")

# Schemas for predict endpoint
class PredictRequest(BaseModel):
    bill_depth_mm: float 
    bill_length_mm: float
    flipper_length_mm: float 
    body_mass_g: float 
    island: str
    sex: str

class PredictResponse(BaseModel): 
    message: str | None = None
    species: str
    latency_ms: int
    model_uri: str

# Endpoints 
@app.get("/health")
def health(): 
    return {"status": "ok", "model_uri": MODEL_URI}

@app.post("/predict", response_model=PredictResponse)
def predict(req: List[PredictRequest]): 
    df = pd.DataFrame([f.model_dump() for f in req])
    t0 = time.time()
    try:
        pred = model.predict(df)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Model inference failed: {e}")

    return {
        "message": f"Species predicted: {pred[0]}",
        "species": pred[0], 
        "latency_ms": int((time.time() - t0) * 1000), 
        "model_uri": MODEL_URI
    }