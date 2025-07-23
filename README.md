# 🔍 Customer Churn Prediction Web App

## 🌐 Overview

This project is a full-stack machine learning web application for **predicting customer churn** using a trained classification model. It consists of:

* A **FastAPI backend** serving ML predictions
* A **Streamlit frontend** for user interaction
* A simple **admin dashboard** with logs, filters, charts, and CSV export
* Built-in logging of predictions with timestamps

It was designed to help business teams easily assess churn risk and make proactive customer retention decisions.

---

## 🧬 Use Case

The application solves a typical telecom business problem: identifying customers likely to churn (i.e., discontinue service) based on usage behavior and profile attributes. Early detection allows timely engagement strategies.

---

## 📆 Project Structure

```
churn-prediction-app/
├── backend/
│   ├── core/
│   │   ├── main.py             # FastAPI app entrypoint
│   │   └── logger.py           # Logging utility
│   ├── churn/
│   │   └── views.py            # API routes for churn prediction
│   └── history/
│       └── predictions.csv     # Prediction logs with timestamps
├── frontend/
│   └── app.py                  # Streamlit UI code
├── model_pipeline/
│   ├── predict.py              # Model loading and prediction logic
│   ├── models/
│   │   └── churn_model.pkl     # Trained ML model (not tracked in Git)
│   └── outputs/
│       └── label_encoders.pkl  # Encoders for categorical features
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Features

### 1. 📊 Prediction API (FastAPI)

* Exposes a POST endpoint at `/api/predict`
* Receives customer data as JSON
* Returns:

  ```json
  {
    "churn": true,
    "probability": 0.82
  }
  ```
* Logs predictions to `backend/history/predictions.csv` with a timestamp

### 2. 📈 Frontend Interface (Streamlit)

* Clean, interactive form for entering customer details
* Instant predictions displayed on submit
* Simple and fast, great for demo or internal use

### 3. 🔧 Admin Dashboard

* Filter predictions by churn status and date
* View as interactive dataframe
* Download logs as CSV
* Visualizations with bar charts and pie charts of predictions

---

## 🤖 Model Details

* Trained on a publicly available customer churn dataset
* Input features include demographics, service usage, and billing preferences
* Model: Logistic Regression / Random Forest (configurable)
* Encoders saved and reused for consistent inference

---

## 🎨 Technologies Used

| Component  | Stack                                |
| ---------- | ------------------------------------ |
| Frontend   | Streamlit                            |
| Backend    | FastAPI                              |
| ML Model   | scikit-learn + joblib                |
| Logging    | Python CSV + UTC timestamps          |
| Deployment | Render / Fly.io / Railway (optional) |

---

## 🚧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/churn-prediction-app.git
cd churn-prediction-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the backend (FastAPI)

```bash
uvicorn backend.core.main:app --reload
```

### 5. Run the frontend (Streamlit)

```bash
streamlit run frontend/app.py
```

### 6. Test the API (optional)

```bash
curl -X POST http://127.0.0.1:8000/api/predict \
     -H "Content-Type: application/json" \
     -d '{"gender": "Male", "SeniorCitizen": 0, ...}'
```

---

## 🔄 Future Improvements

* Replace CSV logging with SQLite/PostgreSQL
* Add JWT/API key authentication
* Dockerize app for portability
* Integrate CI/CD for automated deployment
* Add model monitoring and retraining pipeline

---

## 📄 License

[MIT License](LICENSE)

---

## 👤 Author

**Lawrence Akinboade**
Built as part of a learning path to master end-to-end AI application development.

---

## 📅 Project Status

**Completed MVP** – Frontend, backend, model, logging, admin dashboard all working. Ready for feedback, extension, or deployment.
