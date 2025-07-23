import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# load preprocessed data
X_train = pd.read_csv("model_pipeline/outputs/X_train.csv")
X_test = pd.read_csv("model_pipeline/outputs/X_test.csv")
y_train = pd.read_csv("model_pipeline/outputs/y_train.csv")
y_test = pd.read_csv("model_pipeline/outputs/y_test.csv")

# initialize and train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# predict and evaluate
y_pred = model.predict(X_test)

print("\n Classification Report: \n")
print(classification_report(y_test, y_pred))

print("\n Confusion Matrix: \n")
print(confusion_matrix(y_test, y_pred))

# save model
os.makedirs("model_pipeline/models", exist_ok=True)
joblib.dump(model, "model_pipeline/models/churn_model.pkl")

print("Model training complete. Model saved to model_pipeline/models/churn_model.pkl")