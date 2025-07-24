# backend/api.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
from backend.churn.routes import router as churn_router

app = FastAPI()
app.include_router(churn_router, prefix="/api")

# Load the model and label encoder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "churn", "churn_model.pkl")
encoder_path = os.path.join(BASE_DIR, "churn", "label_encoders.pkl")

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

# Define input schema using Pydantic
class CustomerInput(BaseModel):
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

# Define output schema
class ChurnPrediction(BaseModel):
    churn: bool
    probability: float

@app.get("/")
def home():
    return {"message": "Churn Prediction API is live!"}

@app.post("/predict", response_model=ChurnPrediction)
def predict(data: CustomerInput):
    input_df = pd.DataFrame([data.dict()])

    # Label encoding for 'gender' column only (as an example)
    input_df['gender'] = label_encoder.transform(input_df['gender'])

    # Predict
    churn_prob = model.predict_proba(input_df)[0][1]
    churn = churn_prob > 0.5

    return {"churn": churn, "probability": round(churn_prob, 2)}
