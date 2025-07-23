

import joblib
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "churn", "churn_model.pkl")
encoder_path = os.path.join(BASE_DIR, "churn", "label_encoders.pkl")

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

def predict_churn(data: dict) -> dict:
    df = pd.DataFrame([data])

    # Example: encode 'gender' using label encoder
    df['gender'] = label_encoder.transform(df['gender'])

    proba = model.predict_proba(df)[0][1]
    churn = proba > 0.5

    return {"churn": churn, "probability": round(proba, 2)}
