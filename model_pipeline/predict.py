# model_pipeline/predict.py
import logging
from backend.core.logger import logger  # import the logger
import os
from pathlib import Path
import pickle
import pandas as pd
import numpy as np
import joblib
import csv
from datetime import datetime


# Absolute project root: go two levels up
BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "model_pipeline" / "models" / "churn_model.pkl"
ENCODER_PATH = BASE_DIR / "model_pipeline" / "outputs" / "label_encoders.pkl"

HISTORY_PATH = os.path.abspath(os.path.join(BASE_DIR,'backend', 'history', 'predictions.csv'))
 

def log_prediction(input_data: dict, result: dict):
    """Append prediction result to CSV."""
    fieldnames = list(input_data.keys()) + ["churn", "probability", "timestamp"]
    data_row = {**input_data, **result, "timestamp": datetime.utcnow().isoformat()}

    # Ensure the history directory exists
    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)

    write_header = False
    if not os.path.exists(HISTORY_PATH):
        write_header = True
    else:
        print(f"✅ Writing to: {HISTORY_PATH}")
        print(f"📄 Data Row: {data_row}")
        # Check if file is empty or header is missing
        with open(HISTORY_PATH, "r", newline="") as f:
            try:
                first_line = next(f)
                if "timestamp" not in first_line:
                    write_header = True
            except StopIteration:
                # Empty file
                write_header = True

    with open(HISTORY_PATH, mode="a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(data_row)

    print(f"✅ Wrote prediction with timestamp to: {HISTORY_PATH}")


def make_prediction(input_data: dict):
    try:
        logger.info(f"Received input data: {input_data}")
        df = pd.DataFrame([input_data])
        model = joblib.load(MODEL_PATH)
        encoders = joblib.load(ENCODER_PATH)

        for col, le in encoders.items():
            if col in df.columns:
                try:
                    df[col] = le.transform(df[col])
                except ValueError:
                    raise ValueError(f"Unexpected value in column '{col}': {df[col].values[0]}")

        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]
        logger.info(f"Prediction result: churn={pred}, probability={prob}")
        result = {
            "churn": bool(pred),
            "probability": round(float(prob), 2)
        }
        log_prediction(input_data, result)
        return result
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise





