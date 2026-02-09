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
st.write("Enter patient details to predict heart disease risk")

st.divider()

# ---------------- INPUTS (EXACT ORDER) ----------------
age = st.number_input("Age", min_value=1, max_value=120, value=45)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox(
    "Chest Pain Type",
    options=[0, 1, 2, 3],
    help="0: Typical Angina | 1: Atypical Angina | 2: Non-anginal Pain | 3: Asymptomatic"
)

trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (chol)", 100, 600, 200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox(
    "Resting ECG Results",
    options=[0, 1, 2],
    help="0: Normal | 1: ST-T abnormality | 2: Left ventricular hypertrophy"
)

thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", 60, 220, 150)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    options=[0, 1, 2],
    help="0: Upsloping | 1: Flat | 2: Downsloping"
)

ca = st.selectbox("Number of Major Vessels (ca)", options=[0, 1, 2, 3, 4])

thal = st.selectbox(
    "Thalassemia (thal)",
    options=[0, 1, 2, 3],
    help="0: Normal | 1: Fixed Defect | 2: Reversible Defect | 3: Unknown"
)

# ---------------- PREDICTION ----------------
st.divider()

if st.button("🔍 Predict Heart Disease"):
    try:
        data = np.array([[age, sex, cp, trestbps, chol, fbs,
                          restecg, thalach, exang, oldpeak,
                          slope, ca, thal]])

        result = model.predict(data)[0]

        if result == 1:
            st.error("⚠️ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease Detected")

    except Exception as e:
        st.error("Prediction failed. Please check model or inputs.")
        st.code(str(e))
