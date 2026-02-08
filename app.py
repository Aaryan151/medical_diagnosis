import streamlit as st

st.set_page_config(
    page_title="Intelligent Medical Diagnosis System",
    layout="centered"
)

st.title("🩺 Intelligent Medical Diagnosis System")
st.write("Click on a disease name below to start the prediction.")

st.markdown("---")

st.page_link("pages/1_Heart_Disease.py", label="❤️ Heart Disease", icon="❤️")
st.page_link("pages/2_Lung_Cancer.py", label="🫁 Lung Cancer", icon="🫁")
st.page_link("pages/3_Diabetes.py", label="🩸 Diabetes", icon="🩸")
st.page_link("pages/4_Kidney_Disease.py", label="🧠 Kidney Disease", icon="🧠")
st.page_link("pages/5_Thyroid.py", label="🦋 Thyroid", icon="🦋")
st.page_link("pages/6_Dengue.py", label="🦟 Dengue", icon="🦟")
