import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis System",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
# This CSS targets Streamlit buttons specifically to make them look like your cards
st.markdown("""
<style>
    /* Style the actual Streamlit button to look like a card */
    div.stButton > button {
        background: linear-gradient(135deg, #b31217, #e52d27) !important;
        color: white !important;
        height: 180px !important;
        width: 100% !important;
        border-radius: 20px !important;
        border: none !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
        white-space: normal !important; /* Allows text wrapping */
        padding: 20px !important;
    }

    /* Hover effect */
    div.stButton > button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 12px 30px rgba(229, 45, 39, 0.35) !important;
        border: none !important;
    }

    /* Target the text inside the button */
    div.stButton p {
        font-size: 22px !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div style="background: linear-gradient(90deg,#b31217,#e52d27); padding: 35px; border-radius: 18px; text-align: center; margin-bottom: 40px;">
    <h1 style="color:white; margin-bottom:5px;">Medical Diagnosis System</h1>
    <p style="color:#f2f2f2;">Early detection saves lives</p>
</div>
""", unsafe_allow_html=True)

# ---------- GRID ----------
row1 = st.columns(3)
row2 = st.columns(3)

# Define the cards data for easier rendering
cards = [
    {"label": "❤️ Heart Disease\n\nCardiac risk prediction", "page": "pages/1_Heart_Disease.py", "col": row1[0]},
    {"label": "🫁 Lung Cancer\n\nLung cancer risk assessment", "page": "pages/2_Lung_Cancer.py", "col": row1[1]},
    {"label": "🩸 Diabetes\n\nBlood sugar & diabetes risk", "page": "pages/3_Diabetes.py", "col": row1[2]},
    {"label": "🧠 Kidney Disease\n\nKidney function analysis", "page": "pages/4_Kidney_Disease.py", "col": row2[0]},
    {"label": "🦋 Thyroid\n\nHormonal disorder detection", "page": "pages/5_Thyroid.py", "col": row2[1]},
    {"label": "🦟 Dengue\n\nCBC based dengue detection", "page": "pages/6_Dengue.py", "col": row2[2]},
]

for card in cards:
    with card["col"]:
        if st.button(card["label"], key=card["page"]):
            st.switch_page(card["page"])