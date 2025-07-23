from django.test import TestCase
from rest_framework.test import APIClient

class ChurnApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/predict/'
        self.valid_payload = {
            "gender": "Female",
            "SeniorCitizen": 0,
            "Partner": "Yes",
            "Dependents": "No",
            "tenure": 5,
            "PhoneService": "Yes",
            "MultipleLines": "No",
            "InternetService": "DSL",
            "OnlineSecurity": "No",
            "OnlineBackup": "Yes",
            "DeviceProtection": "No",
            "TechSupport": "No",
            "StreamingTV": "No",
            "StreamingMovies": "No",
            "Contract": "Month-to-month",
            "PaperlessBilling": "Yes",
            "PaymentMethod": "Mailed check",
            "MonthlyCharges": 45.2,
            "TotalCharges": 250.5
        }

    def test_predict_endpoint_returns_valid_response(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('churn', response.data)
        self.assertIn('probability', response.data)
