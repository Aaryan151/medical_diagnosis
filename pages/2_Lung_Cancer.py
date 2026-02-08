import streamlit as st
import numpy as np
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Lung Cancer", layout="centered")
st.title("🫁 Lung Cancer Prediction")
st.markdown("---")

# ---------------- LOAD MODEL ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "lung_cancer_model.pkl")

model = joblib.load(MODEL_PATH)

# ---------------- INPUTS (SCALE 1–8) ----------------
Alcohol_Use = st.slider("Alcohol Use", 1, 8, 4)
Dust_Allergy = st.slider("Dust Allergy", 1, 8, 4)
Balanced_Diet = st.slider("Balanced Diet", 1, 8, 4)
Obesity = st.slider("Obesity", 1, 8, 4)
Smoking = st.slider("Smoking", 1, 8, 4)
Passive_Smoker = st.slider("Passive Smoker", 1, 8, 4)
Coughing_Blood = st.slider("Coughing Of Blood", 1, 8, 4)
Fatigue = st.slider("Fatigue", 1, 8, 4)
Shortness_Breath = st.slider("Shortness Of Breath", 1, 8, 4)
Wheezing = st.slider("Wheezing", 1, 8, 4)
Swallowing_Difficulty = st.slider("Swallowing Difficulty", 1, 8, 4)
Clubbing_Finger_Nails = st.slider("Clubbing Of Finger Nails", 1, 8, 4)

# ---------------- PREDICTION ----------------
if st.button("Predict Lung Cancer"):

    data = np.array([[
        Alcohol_Use,
        Dust_Allergy,
        Balanced_Diet,
        Obesity,
        Smoking,
        Passive_Smoker,
        Coughing_Blood,
        Fatigue,
        Shortness_Breath,
        Wheezing,
        Swallowing_Difficulty,
        Clubbing_Finger_Nails
    ]])

    result = model.predict(data)[0]

    # ---------------- OUTPUT MAPPING ----------------
    if result == 0:
        st.success("🟢 Low Risk of Lung Cancer")
    elif result == 1:
        st.warning("🟡 Medium Risk of Lung Cancer")
    elif result == 2:
        st.error("🔴 High Risk of Lung Cancer")
    else:
        st.info("⚠️ Unable to determine risk level")
