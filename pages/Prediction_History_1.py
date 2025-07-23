import pandas as pd
import streamlit as st
import os

csv_path = "backend/history/predictions.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    if "timestamp" in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp', ascending=False)

    st.subheader("Prediction History")
    st.dataframe(df)
else:
    st.warning("No prediction history found yet.")
