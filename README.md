# 📊 Customer Churn Prediction App

## Overview

This project is a full-stack machine learning application designed to predict customer churn for a telecom company. It combines a FastAPI backend for model inference with a Streamlit frontend for user interaction. The entire application is deployed on Render.

The goal is to assist businesses in identifying customers likely to leave their service so that proactive retention strategies can be implemented.

---

## 🚀 Features

- **Churn Prediction** using a trained ML model.
- **User-Friendly Interface** via Streamlit.
- **Real-time Predictions** with a deployed FastAPI API.
- **Admin Dashboard** to monitor prediction logs.
- **Data Persistence** using CSV logging.
- **Render Deployment** for public accessibility.

---

## 🧠 Machine Learning

- **Model**: Logistic Regression (or your chosen classifier).
- **Input Features**: 19 customer attributes including:
  - Demographics (e.g., gender, senior citizen)
  - Services used (e.g., InternetService, StreamingTV)
  - Billing information (e.g., MonthlyCharges, PaymentMethod)
- **Encoding**: Categorical columns are label-encoded using a saved encoder.

---

## 📁 Project Structure

```
.
├── backend
│   ├── churn
│   │   ├── churn_model.pkl
│   │   ├── label_encoders.pkl
│   │   ├── routes.py
│   │   └── schemas.py
│   └── core
│       └── main.py
│   └── api.py
├── frontend
│   └── app.py
├── predictions.csv
├── requirements.txt
└── README.md
```

---

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/churn-prediction-app.git
   cd churn-prediction-app
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend API**  
   ```bash
   uvicorn backend.api:app --reload
   ```

5. **Run the frontend (in another terminal)**  
   ```bash
   streamlit run frontend/app.py
   ```

---

## 🌐 Deployment

The app is deployed using **Render**. You can access it at:

👉 **Frontend**: [your-streamlit-url]  
👉 **API**: [your-api-url]

Make sure to update the frontend to send requests to the correct `POST /predict` endpoint.

---

## 📊 Admin Features

- View all past predictions
- Filter by churn probability
- Export logs as CSV

---

## 🔍 Future Work

- Add user authentication for admin dashboard.
- Implement live model retraining using feedback.
- Integrate with cloud storage (e.g., S3) for scalable logging.
- Improve model performance with advanced algorithms (XGBoost, Neural Nets).

---

## 🧑‍💻 Author

- **Lawrence Akinboade** — aspiring AI engineer | [LinkedIn](#) | [GitHub](#)

---

## 📄 License

This project is licensed under the MIT License.