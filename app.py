import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis System",
    layout="centered"
)

st.title("🩺 Intelligent Medical Diagnosis System")
st.write("Select a disease from the left sidebar to start prediction.")

st.markdown("---")

st.markdown("""
### Available Disease Models:
- ❤️ Heart Disease
- 🧠 Kidney Disease
- 🍬 Diabetes
- 🦋 Thyroid
- 🫁 Lung Cancer
- 🦟 Dengue

👈 Use the **sidebar menu** to navigate.
""")
