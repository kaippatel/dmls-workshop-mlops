from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from mlflow.tracking import MlflowClient
import mlflow.pyfunc
import mlflow
import pandas as pd
import time 
from pathlib import Path

APP_DIR = Path(__file__).parent
mlflow.set_tracking_uri("http://localhost:5000")
model = mlflow.pyfunc.load_model(str(APP_DIR / "artifacts"))

app = FastAPI(title="Titanic Classifier API")

# ---------DO NOT CHANGE---------------
class Request(BaseModel):
    pclass: int
    sex: str
    age: Optional[float] = None
    sibsp: int
    parch: int
    fare: Optional[float] = None
    embarked: Optional[str] = Field(None, description="S/C/Q")
    embark_town: Optional[str] = Field(None, description="Southampton/Cherbourg/Queenstown")
    class_: Optional[str] = Field(None, alias="class")  
    who: Optional[str] = None                         
    adult_male: Optional[bool] = None
    deck: Optional[str] = None                         
    alone: Optional[bool] = None

    model_config = {"populate_by_name": True}

class Response(BaseModel): 
    message: str | None = None
    survived: int
    latency_ms: int

# Endpoints 
@app.get("/health")
def health(): 
    try:
        _ = model
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {e}")
    
    return {
        "status": "ok", 
        "model_file": "model.pkl",
        "framework": "sklearn",
    }

@app.post("/predict", response_model=Response)
def predict(req: Request): 
    df = pd.DataFrame([req.model_dump(by_alias=True)])  
    t0 = time.time()
    try:
        y = model.predict(df)
        pred = int(y[0])
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Model inference failed: {e}")
    
    return {
        "message": f"Passenger survival predicted: {pred}",
        "survived": pred, 
        "latency_ms": int((time.time() - t0) * 1000), 
    }