# backend/churn/routes.py

from fastapi import APIRouter
from .schemas import CustomerInput, ChurnPrediction
from .service import predict_churn

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "Welcome to the Churn Prediction API!"}

@router.post("/predict", response_model=ChurnPrediction)
def predict(input_data: CustomerInput):
    result = predict_churn(input_data.dict())
    return result
