import joblib
import numpy as np
import pandas as pd
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import ChurnInputSerializer




# # Load model and encoders once(at server startup)
# model = joblib.load("churn/churn_model.pkl")
# encoders = joblib.load("churn/label_encoders.pkl")

# # Expected feature order( to match training)
# FEATURES = [
#     'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 
#     'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
#     'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 
#     'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
#     'MonthlyCharges', 'TotalCharges'
# ]

# # Create your views here.
# @api_view(['POST'])
# def predict_churn(request):
#     serializer = ChurnInputSerializer(data=request.data)
    
#     if not serializer.is_valid():
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         # Use validated input
#         input_data = serializer.validated_data
#         input_df = pd.DataFrame([input_data])[FEATURES]

#         # Encode categorical columns
#         for col in encoders:
#             input_df[col] = encoders[col].transform(input_df[col])

#         # Predict
#         pred = model.predict(input_df)[0]
#         prob = model.predict_proba(input_df)[0][1]

#         return Response({
#             "churn": bool(pred),
#             "probability": round(float(prob), 4)
#         })

#     except Exception as e:
#         return Response(
#             {"error": str(e)},
#             status=status.HTTP_400_BAD_REQUEST
#         )


# backend/churn/views.py

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
