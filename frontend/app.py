# app.py

import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("Customer Churn Prediction App")

# 👤 User inputs
st.subheader("Enter customer information")

form = st.form("prediction_form")
gender = form.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = form.selectbox("Senior Citizen", [0, 1])
Partner = form.selectbox("Partner", ["Yes", "No"])
Dependents = form.selectbox("Dependents", ["Yes", "No"])
tenure = form.number_input("Tenure (months)", 0, 72)
PhoneService = form.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = form.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = form.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = form.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = form.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = form.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = form.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = form.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = form.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = form.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = form.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = form.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
MonthlyCharges = form.number_input("Monthly Charges", 0.0, 1000.0)
TotalCharges = form.number_input("Total Charges", 0.0, 10000.0)

submitted = form.form_submit_button("Predict")

# 🔮 Predict
if submitted:
    with st.spinner("Making prediction..."):
        input_data = {
            "gender": gender,
            "SeniorCitizen": SeniorCitizen,
            "Partner": Partner,
            "Dependents": Dependents,
            "tenure": tenure,
            "PhoneService": PhoneService,
            "MultipleLines": MultipleLines,
            "InternetService": InternetService,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "StreamingTV": StreamingTV,
            "StreamingMovies": StreamingMovies,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "PaymentMethod": PaymentMethod,
            "MonthlyCharges": MonthlyCharges,
            "TotalCharges": TotalCharges,
        }

        try:
            response = requests.post("https://churn-predictor-15.onrender.com/predict", json=input_data)
            response.raise_for_status()
            result = response.json()

            st.success("Prediction complete!")
            st.write(f"**Will churn:** `{result['churn']}`")
            st.write(f"**Probability:** `{result['probability']}`")

        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")
