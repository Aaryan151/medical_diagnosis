import streamlit as st

import numpy as np

import joblib



st.set_page_config(page_title="Diabetes", layout="centered")

st.title("🩸 Diabetes Prediction")



# ---------- LOAD PKL ----------

obj = joblib.load("models/diabetes_model.pkl")



# Handle dict-based pkl

if isinstance(obj, dict):

    if "model" in obj:

        model = obj["model"]

    elif "classifier" in obj:

        model = obj["classifier"]

    else:

        st.error("❌ No valid model found inside PKL file")

        st.stop()

else:

    model = obj



# ---------- INPUTS ----------

Pregnancies = st.number_input("Pregnancies", 0, 20, 1)

Glucose = st.number_input("Glucose", 0, 300, 150)

BloodPressure = st.number_input("Blood Pressure", 0, 200, 80)

SkinThickness = st.number_input("Skin Thickness", 0, 100, 20)

Insulin = st.number_input("Insulin", 0, 900, 80)

BMI = st.number_input("BMI", 0.0, 70.0, 25.0)

DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)

Age = st.number_input("Age", 1, 120, 33)



# ---------- PREDICTION ----------

if st.button("Predict Diabetes"):

    data = np.array([[Pregnancies, Glucose, BloodPressure,

                      SkinThickness, Insulin, BMI,

                      DiabetesPedigreeFunction, Age]])



    try:

        result = model.predict(data)[0]



        if result == 1:

            st.error("⚠️ Diabetes Detected")

        else:

            st.success("✅ No Diabetes Detected")



    except Exception as e:

        st.error("Prediction failed. Feature mismatch or invalid model.")

        st.code(str(e))