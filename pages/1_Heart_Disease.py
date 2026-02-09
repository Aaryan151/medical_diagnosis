import streamlit as st
import numpy as np
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("models/heart_model.pkl")

# ---------------- TITLE ----------------
st.title("❤️ Heart Disease Prediction")
st.write("Enter patient details to predict heart disease")

st.divider()

# ---------------- INPUTS ----------------

age = st.number_input("Age", min_value=1, max_value=120, value=45)

sex = st.selectbox("Sex", ["F", "M"])
sex = 1 if sex == "M" else 0

cp = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)
cp_map = {"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3}
cp = cp_map[cp]

resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)

chol = st.number_input("Cholesterol", 0, 600, 200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
fbs = 1 if fbs == "Yes" else 0

rest_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)
restecg_map = {"LVH": 0, "Normal": 1, "ST": 2}
rest_ecg = restecg_map[rest_ecg]

max_hr = st.number_input("Max Heart Rate", 60, 220, 150)

ex_angina = st.selectbox("Exercise Induced Angina", ["N", "Y"])
ex_angina = 1 if ex_angina == "Y" else 0

oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 10.0, 1.0)

st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])
slope_map = {"Down": 0, "Flat": 1, "Up": 2}
st_slope = slope_map[st_slope]

# ---------------- PREDICTION ----------------
st.divider()

if st.button("🔍 Predict"):
    try:
        data = np.array([[age, sex, cp, resting_bp, chol, fbs,
                          rest_ecg, max_hr, ex_angina,
                          oldpeak, st_slope]])

        prediction = model.predict(data)[0]

        if prediction == 1:
            st.error("⚠️ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease Detected")

    except Exception as e:
        st.error("Prediction failed")
        st.code(str(e))
