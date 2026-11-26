# app.py
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# 📂 Load model from the same folder as app.py (works from any terminal location)
MODEL_PATH = Path(__file__).parent / 'risk_model.pkl'
art = joblib.load(MODEL_PATH)

st.title("🚨 Risk Alert Classifier")
st.write("Enter customer details to predict whether the customer is **High Risk**.")

# Sidebar inputs (numeric default = training median)
data = {}
st.sidebar.header("Customer Details")
for c in art['num_cols']:
    data[c] = st.sidebar.number_input(c, value=float(art['medians'][c]))
for c in art['cat_cols']:
    data[c] = st.sidebar.selectbox(c, art['cat_options'][c])

if st.button("🔍 Predict Risk"):
    row = pd.DataFrame([data])
    row = pd.get_dummies(row, columns=art['cat_cols'], dtype=int)
    row = row.reindex(columns=art['columns'], fill_value=0)   # same training columns

    row_s = art['scaler'].transform(row)        # scale
    row_s = art['imputer'].transform(row_s)     # imputer (safe)

    prob = art['model'].predict_proba(row_s)[0, 1]
    if prob >= 0.5:
        st.error(f"⚠️ High Risk Customer (Probability: {prob:.2%})")
    else:
        st.success(f"✅ Low Risk Customer (Probability: {prob:.2%})")
