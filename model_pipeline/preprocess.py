import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# create output directory if it doesnt exist
os.makedirs("model_pipeline/outputs", exist_ok=True)

# load data
df = pd.read_csv("data/telco-churn.csv")

# Drop customerID (not useful for prediction)
df.drop("customerID", axis=1, inplace=True)

# convert totalcharges to numeric ( some empty strings)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# fill missing totalcharges with 0
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# conver target to binary (yes -> 1, no -> 0)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Separate target and features
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Encode categorical variables
cat_cols = X.select_dtypes(include=["object"]).columns
encoders = {}

for col in cat_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# save encoders to disk
joblib.dump(encoders, "model_pipeline/outputs/label_encoders.pkl")

# Train/Test splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save preprocessed data
X_train.to_csv("model_pipeline/outputs/X_train.csv", index=False)
X_test.to_csv("model_pipeline/outputs/X_test.csv", index=False)
y_train.to_csv("model_pipeline/outputs/y_train.csv", index=False)
y_test.to_csv("model_pipeline/outputs/y_test.csv", index=False)

print("Data Preprocessing Complete. Files saved in model_pipeline/outputs/")
