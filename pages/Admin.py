# admin.py

import streamlit as st
import pandas as pd
import os

from datetime import datetime

CSV_PATH = "backend/history/predictions.csv"

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("🛠️ Admin Dashboard - Prediction Monitor")

# Load CSV
if not os.path.exists(CSV_PATH):
    st.error("❌ predictions.csv not found.")
    st.stop()

df = pd.read_csv(CSV_PATH)

# Quick sanity check
st.write("✅ Raw predictions loaded:", len(df))

if df.empty or "timestamp" not in df.columns:
    st.warning("⚠️ No prediction data available or 'timestamp' column missing.")
    st.stop()

# Parse timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.dropna(subset=['timestamp'])  # Drop rows with invalid timestamps

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    start_date = st.date_input("Start Date", value=df['timestamp'].min().date())
    end_date = st.date_input("End Date", value=df['timestamp'].max().date())
    churn_filter = st.selectbox("Churn Outcome", options=["All", "True", "False"])
    search_query = st.text_input("Search (e.g., 'Yes', 'DSL')")

# Apply filters
mask = (df['timestamp'].dt.date >= start_date) & (df['timestamp'].dt.date <= end_date)
if churn_filter != "All":
    mask &= df['churn'].astype(str) == churn_filter

if search_query:
    mask &= df.astype(str).apply(lambda row: search_query.lower() in row.to_string().lower(), axis=1)

filtered_df = df[mask]

# Add fallback if no results
if filtered_df.empty:
    st.warning("🚫 No results for selected filters.")
    st.stop()

# Summary Metrics
st.subheader("📊 Summary Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Predictions", len(filtered_df))
col2.metric("Churned", filtered_df["churn"].sum())
col3.metric("Avg. Probability", round(filtered_df["probability"].mean(), 2))

# Churn Over Time
st.subheader("📈 Churn Trends")
daily = filtered_df.set_index('timestamp').resample('D').agg({
    'churn': 'sum',
    'probability': 'mean'
}).rename(columns={'churn': 'Churn Count', 'probability': 'Avg. Probability'})

st.line_chart(daily)

import plotly.express as px  # Add this to your imports if not already

# --- Pie Chart: Churn Distribution ---
st.subheader("🥧 Churn Distribution")
pie = px.pie(
    filtered_df,
    names="churn",
    title="Churn vs No-Churn",
    color_discrete_sequence=["#EF553B", "#00CC96"],
    hole=0.4  # Makes it a donut chart
)
st.plotly_chart(pie, use_container_width=True)


# --- Bar Chart: Churn Count by Contract Type ---
if "Contract" in filtered_df.columns:
    st.subheader("📊 Churn by Contract Type")
    bar_df = filtered_df.groupby(["Contract", "churn"]).size().reset_index(name="count")
    bar = px.bar(
        bar_df,
        x="Contract",
        y="count",
        color="churn",
        barmode="group",
        title="Churn Counts by Contract Type",
        color_discrete_sequence=["#00CC96", "#EF553B"],
    )
    st.plotly_chart(bar, use_container_width=True)


# Full Table
st.subheader("🧾 Prediction Log")
st.dataframe(filtered_df.sort_values(by='timestamp', ascending=False), use_container_width=True)

# Download
csv = filtered_df.to_csv(index=False)
st.download_button("📥 Download Filtered CSV", csv, "filtered_predictions.csv", "text/csv")


st.subheader("⬇️ Download Predictions")


export_all = st.checkbox("Export all predictions", value=False)
export_df = df if export_all else filtered_df
csv = export_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="filtered_predictions.csv",
    mime="text/csv",
    help="Exports the filtered table data"
)
