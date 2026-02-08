import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Diabetes", layout="centered")
st.title("🩸 Diabetes Prediction")

model = joblib.load("models/diabetes_model.pkl")

st.markdown("---")

Pregnancies = st.number_input("Pregnancies", 0, 20, 1)
Glucose = st.number_input("Glucose", 0, 300, 120)
Blood_Pressure = st.number_input("Blood Pressure", 0, 200, 70)
Skin_Thickness = st.number_input("Skin Thickness", 0, 100, 20)
Insulin = st.number_input("Insulin", 0, 900, 80)
BMI = st.number_input("BMI", 0.0, 70.0, 25.0)
DPF = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
Age = st.number_input("Age", 1, 120, 33)

if st.button("Predict Diabetes"):
    data = np.array([[Pregnancies, Glucose, Blood_Pressure,
                      Skin_Thickness, Insulin, BMI, DPF, Age]])

    result = model.predict(data)[0]

    if result == 1:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Non-Diabetic")
