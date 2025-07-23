from django.test import TestCase
import pandas as pd
import joblib

class ChurnModelTest(TestCase):
    def setUp(self):
        self.model = joblib.load('churn/churn_model.pkl')
        self.encoders = joblib.load('churn/label_encoders.pkl')

        self.sample = {
            "gender": "Male",
            "SeniorCitizen": 0,
            "Partner": "Yes",
            "Dependents": "No",
            "tenure": 12,
            "PhoneService": "Yes",
            "MultipleLines": "No",
            "InternetService": "DSL",
            "OnlineSecurity": "Yes",
            "OnlineBackup": "No",
            "DeviceProtection": "No",
            "TechSupport": "No",
            "StreamingTV": "Yes",
            "StreamingMovies": "Yes",
            "Contract": "Month-to-month",
            "PaperlessBilling": "Yes",
            "PaymentMethod": "Electronic check",
            "MonthlyCharges": 70.35,
            "TotalCharges": 845.5
        }

    def test_model_predicts_without_error(self):
        df = pd.DataFrame([self.sample])

        for col, encoder in self.encoders.items():
            df[col] = encoder.transform(df[col])

        result = self.model.predict(df)[0]
        self.assertIn(result, [0, 1])
