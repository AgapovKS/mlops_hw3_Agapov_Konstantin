import os
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

MODEL_VERSION = os.getenv("MODEL_VERSION", "v1.0.0")
model = joblib.load("model.pkl")

class Input(BaseModel):
    x: list[float]

@app.get("/health")
def health():
    return {"status": "ok", "version": MODEL_VERSION}

@app.post("/predict")
def predict(data: Input):
    pred = model.predict([data.x])
    return {
        "prediction": pred.tolist(),
        "version": MODEL_VERSION
    }
