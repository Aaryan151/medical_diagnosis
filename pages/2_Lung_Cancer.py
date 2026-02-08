import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Lung Cancer", layout="centered")
st.title("🫁 Lung Cancer Prediction")

model = joblib.load("models/lung_model.pkl")

st.markdown("---")

Alcohol_Use = st.selectbox("Alcohol Use", [0, 1])
Dust_Allergy = st.selectbox("Dust Allergy", [0, 1])
Balanced_Diet = st.selectbox("Balanced Diet", [0, 1])
Obesity = st.selectbox("Obesity", [0, 1])
Smoking = st.selectbox("Smoking", [0, 1])
Passive_Smoker = st.selectbox("Passive Smoker", [0, 1])
Coughing_Blood = st.selectbox("Coughing Of Blood", [0, 1])
Fatigue = st.selectbox("Fatigue", [0, 1])
Shortness_Breath = st.selectbox("Shortness Of Breath", [0, 1])
Wheezing = st.selectbox("Wheezing", [0, 1])
Swallowing_Difficulty = st.selectbox("Swallowing Difficulty", [0, 1])
Clubbing_Finger_Nails = st.selectbox("Clubbing Of Finger Nails", [0, 1])

if st.button("Predict Lung Cancer"):
    data = np.array([[Alcohol_Use, Dust_Allergy, Balanced_Diet, Obesity,
                      Smoking, Passive_Smoker, Coughing_Blood, Fatigue,
                      Shortness_Breath, Wheezing,
                      Swallowing_Difficulty, Clubbing_Finger_Nails]])

    result = model.predict(data)[0]

    if result == 1:
        st.error("⚠️ High Risk of Lung Cancer")
    else:
        st.success("✅ Low Risk of Lung Cancer")
