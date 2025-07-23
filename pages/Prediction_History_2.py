import streamlit as st
import pandas as pd
import os

st.title("🕒 Prediction History")

# Path to CSV
csv_path = os.path.join("backend", "history", "predictions.csv")

# Check if the file exists
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    # Make sure 'timestamp' is parsed correctly
    if 'timestamp' in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Display filters
        st.sidebar.header("Filter Predictions")
        churn_filter = st.sidebar.selectbox("Churn Outcome", options=["All", "True", "False"])

        if churn_filter != "All":
            df = df[df["churn"] == (churn_filter == "True")]

        # Show dataframe
        st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)

        # Summary Stats
        st.subheader("📊 Summary")
        st.metric("Total Predictions", len(df))
        st.metric("Churned", df["churn"].sum())
        st.metric("Churn Probability ≥ 0.8", (df["probability"] >= 0.8).sum())

    else:
        st.error("❌ 'timestamp' column not found in the CSV.")
else:
    st.warning("📂 No prediction history file found yet.")
