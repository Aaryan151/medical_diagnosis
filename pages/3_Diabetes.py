import streamlit as st
import numpy as np
import joblib

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #e52d27;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🩸 Diabetes Prediction")
st.write("Enter the patient's clinical metrics below to assess the risk of diabetes.")

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    try:
        obj = joblib.load("models/diabetes_model.pkl")
        # Handle dict-based pkl or direct model object
        if isinstance(obj, dict):
            if "model" in obj: return obj["model"]
            if "classifier" in obj: return obj["classifier"]
            return None
        return obj
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

if model is None:
    st.error("❌ Model file not found or invalid. Please check the 'models/' folder.")
    st.stop()

# ---------- INPUT FORM ----------
# Using columns to make the form look cleaner
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    BloodPressure = st.number_input("Blood Pressure (mm Hg)", 0, 200, 80)
    Insulin = st.number_input("Insulin (mu U/ml)", 0, 900, 80)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree (DPF)", 0.0, 3.0, 0.5)

with col2:
    Glucose = st.number_input("Glucose (mg/dL)", 0, 300, 150)
    SkinThickness = st.number_input("Skin Thickness (mm)", 0, 100, 20)
    BMI = st.number_input("Body Mass Index (BMI)", 0.0, 70.0, 25.0)
    Age = st.number_input("Age (Years)", 1, 120, 33)

st.divider()

# ---------- PREDICTION LOGIC ----------
if st.button("Analyze Results"):
    # 1. Arrange features in the EXACT order the model was trained on:
    # Typical order: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age
    features = np.array([[
        Pregnancies, Glucose, BloodPressure, SkinThickness, 
        Insulin, BMI, DiabetesPedigreeFunction, Age
    ]])

    try:
        # 2. Get the real prediction from the model
        prediction = model.predict(features)[0]
        
        # 3. Get probability if the model supports it (optional but helpful)
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(features)[0][1] * 100
        else:
            probability = None

        # 4. Display results based on the prediction
        if prediction == 1:
            st.error(f"### ⚠️ Result: Diabetes Detected")
            if probability:
                st.write(f"Confidence Level: **{probability:.2f}%**")
            st.warning("Please consult a medical professional for further clinical testing.")
        else:
            st.success(f"### ✅ Result: No Diabetes Detected")
            if probability:
                st.write(f"Confidence Level: **{100 - probability:.2f}%**")
            st.info("The metrics provided fall within the low-risk range according to the model.")

    except Exception as e:
        st.error("An error occurred during prediction.")
        st.info("This often happens if the input features don't match the model's training format.")
        st.code(str(e))

# ---------- FOOTER ----------
st.markdown("---")
if st.button("⬅️ Back to Dashboard"):
    st.switch_page("app.py") # Make sure this matches your main filename