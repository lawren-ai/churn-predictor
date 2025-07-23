

from fastapi import FastAPI
from churn.views import router as churn_router

app = FastAPI(
    title="Churn Prediction API",
    version="1.0.0",
)

# Register routes
app.include_router(churn_router, prefix="/api")


from fastapi import FastAPI
from churn.schemas import CustomerData
from model_pipeline.predict import make_prediction

app = FastAPI()

@app.post("/api/predict")
def predict(data: CustomerData):
    input_dict = data.dict()
    result = make_prediction(input_dict)
    return result

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
