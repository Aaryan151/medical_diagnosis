import streamlit as st
import numpy as np
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Dengue", layout="centered")
st.title("🦟 Dengue Prediction (CBC Based)")
st.markdown("---")

# ---------------- LOAD MODEL ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "dengue_diagnosis_model.pkl")

model = joblib.load(MODEL_PATH)
st.error(f"MODEL EXPECTS: {model.n_features_in_} FEATURES")


# ---------------- INPUTS ----------------
Age = st.number_input("Age", 1, 120, 25)

Hemoglobin = st.number_input("Hemoglobin", 5.0, 20.0, 13.0)
RBC = st.number_input("RBC (million/µL)", 2.0, 7.0, 4.5)
HCT = st.number_input("Hematocrit (HCT)", 20.0, 60.0, 40.0)

MCV = st.number_input("MCV", 60.0, 110.0, 85.0)
MCH = st.number_input("MCH", 20.0, 40.0, 28.0)
MCHC = st.number_input("MCHC", 25.0, 40.0, 33.0)

RDW_CV = st.number_input("RDW-CV", 10.0, 20.0, 13.0)

WBC = st.number_input("WBC Count", 2000, 20000, 7000)

Neutrophils = st.number_input("Neutrophils (%)", 0.0, 100.0, 55.0)
Lymphocytes = st.number_input("Lymphocytes (%)", 0.0, 100.0, 35.0)
Monocytes = st.number_input("Monocytes (%)", 0.0, 20.0, 5.0)

Platelet = st.number_input("Platelet Count", 10000, 500000, 150000)
PDW = st.number_input("PDW", 5.0, 25.0, 15.0)
MPV = st.number_input("MPV", 5.0, 15.0, 9.0)
PCT = st.number_input("PCT", 0.0, 1.0, 0.25)

Gender = st.selectbox("Gender", ["Female", "Male"])
Gender_Male = 1 if Gender == "Male" else 0

# ---------------- PREDICTION ----------------
if st.button("Predict Dengue"):

    # ⚠️ EXACT FEATURE ORDER (MATCHES TRAINING)
    data = np.array([[
        Age,            # 1
        Hemoglobin,     # 2
        RBC,            # 3
        HCT,            # 4
        MCV,            # 5
        MCH,            # 6
        MCHC,           # 7
        RDW_CV,         # 8
        WBC,            # 9
        Neutrophils,    # 10
        Lymphocytes,    # 11
        Monocytes,      # 12
        Platelet,       # 13
        PDW,            # 14
        MPV,            # 15
        PCT,            # 16
        Gender_Male     # 17  ✅ MUST BE LAST
    ]])

    result = model.predict(data)[0]

    if result == 1:
        st.error("⚠️ Dengue Detected")
    else:
        st.success("✅ No Dengue Detected")
