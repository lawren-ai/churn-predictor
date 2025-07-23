import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the predictions CSV file
PREDICTIONS_CSV = os.path.abspath(os.path.join("..", "backend", "history", "predictions.csv"))

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("📊 Admin Dashboard - Customer Churn Insights")

# Load the data
@st.cache_data
def load_predictions():
    try:
        df = pd.read_csv(PREDICTIONS_CSV)
        return df
    except Exception as e:
        st.warning(f"Error loading predictions: {e}")
        return pd.DataFrame()

df = load_predictions()

if df.empty:
    st.info("No predictions logged yet.")
else:
    # Filters
    with st.sidebar:
        st.header("🔍 Filter Options")
        gender_filter = st.multiselect("Gender", options=df["gender"].unique(), default=df["gender"].unique())
        churn_filter = st.multiselect("Churn", options=[True, False], default=[True, False])
        df = df[df["gender"].isin(gender_filter) & df["churn"].isin(churn_filter)]

    # Download
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "filtered_predictions.csv", "text/csv")

    # Charts
    st.subheader("📈 Churn Distribution")
    churn_counts = df["churn"].value_counts()
    st.bar_chart(churn_counts)

    # Table
    st.subheader("🗂️ Filtered Predictions")
    st.dataframe(df, use_container_width=True)
