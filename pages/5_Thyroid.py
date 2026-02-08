import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Thyroid", layout="centered")
st.title("🦋 Thyroid Disease Prediction")

model = joblib.load("models/thyroid_model.pkl")
st.write("Model expects:", model.n_features_in_)


st.markdown("---")

Age = st.number_input("Age", 1, 120, 35)
Sex = st.selectbox("Sex", ["Female", "Male"])
On_Thyroxine = st.selectbox("On Thyroxine", ["No", "Yes"])
On_Anti = st.selectbox("On Anti-thyroid Medication", ["No", "Yes"])
TSH = st.number_input("TSH", 0.0, 100.0, 2.5)
TT4 = st.number_input("TT4", 0.0, 300.0, 100.0)
T4U = st.number_input("T4U", 0.0, 2.0, 1.0)
FTI = st.number_input("FTI", 0.0, 300.0, 100.0)

Sex = 1 if Sex == "Male" else 0
On_Thyroxine = 1 if On_Thyroxine == "Yes" else 0
On_Anti = 1 if On_Anti == "Yes" else 0

if st.button("Predict Thyroid Disease"):
    data = np.array([[Age, Sex, On_Thyroxine, On_Anti,
                      TSH, TT4, T4U, FTI]])

    result = model.predict(data)[0]

    if result == 1:
        st.error("⚠️ Thyroid Disorder Detected")
    else:
        st.success("✅ Normal Thyroid")
