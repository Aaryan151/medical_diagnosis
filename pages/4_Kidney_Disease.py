import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Kidney Disease", layout="centered")
st.title("🧠 Kidney Disease Prediction")

model = joblib.load("models/kidney_model.pkl")

st.markdown("---")

Bp = st.number_input("Blood Pressure (Bp)", 50, 200, 80)
Sg = st.number_input("Specific Gravity (Sg)", 1.0, 1.05, 1.02)
Al = st.selectbox("Albumin (Al)", [0, 1, 2, 3, 4, 5])
Su = st.selectbox("Sugar (Su)", [0, 1, 2, 3, 4, 5])
Rbc = st.selectbox("Red Blood Cells (Rbc)", [0, 1])
Bu = st.number_input("Blood Urea (Bu)", 1, 300, 40)
Sc = st.number_input("Serum Creatinine (Sc)", 0.1, 15.0, 1.2)
Sod = st.number_input("Sodium (Sod)", 100, 200, 135)
Pot = st.number_input("Potassium (Pot)", 2.0, 10.0, 4.5)
Hemo = st.number_input("Hemoglobin (Hemo)", 3.0, 20.0, 13.5)
Wbcc = st.number_input("WBC Count (Wbcc)", 3000, 20000, 8000)
Rbcc = st.number_input("RBC Count (Rbcc)", 2.0, 7.0, 4.5)
Htn = st.selectbox("Hypertension (Htn)", [0, 1])

if st.button("Predict Kidney Disease"):
    data = np.array([[Bp, Sg, Al, Su, Rbc, Bu, Sc,
                      Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])

    result = model.predict(data)[0]

    if result == 1:
        st.error("⚠️ Kidney Disease Detected")
    else:
        st.success("✅ Healthy Kidneys")
