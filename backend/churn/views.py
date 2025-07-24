import joblib
import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import sys
# Add the root project directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from model_pipeline.predict import make_prediction

router = APIRouter()

# Define request schema using Pydantic
class ChurnInput(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@router.post("/predict")
async def predict_churn(input_data: ChurnInput):
    try:
        prediction = make_prediction(input_data.dict())
        return prediction
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
