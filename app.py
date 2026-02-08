import streamlit as st

st.set_page_config(
    page_title="Intelligent Medical Diagnosis System",
    layout="wide"
)

st.title("🩺 Intelligent Medical Diagnosis System")
st.write("Click on a disease to start prediction")

st.markdown("---")

# ---------- CSS FOR BIG CLICKABLE BOX ----------
st.markdown("""
<style>
.card {
    background: linear-gradient(145deg, #0f172a, #020617);
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}
.card h2 {
    margin: 0;
    font-size: 26px;
}
.card p {
    color: #94a3b8;
    margin-top: 8px;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/1_Heart_Disease.py", label="❤️ Heart Disease", icon="❤️")
    st.markdown("<p>Cardiac risk prediction</p></div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/2_Lung_Cancer.py", label="🫁 Lung Cancer", icon="🫁")
    st.markdown("<p>Lung cancer risk assessment</p></div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/3_Diabetes.py", label="🩸 Diabetes", icon="🩸")
    st.markdown("<p>Blood sugar & diabetes risk</p></div>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/4_Kidney_Disease.py", label="🧠 Kidney Disease", icon="🧠")
    st.markdown("<p>Kidney function analysis</p></div>", unsafe_allow_html=True)

with col5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/5_Thyroid.py", label="🦋 Thyroid", icon="🦋")
    st.markdown("<p>Hormonal disorder detection</p></div>", unsafe_allow_html=True)

with col6:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/6_Dengue.py", label="🦟 Dengue", icon="🦟")
    st.markdown("<p>CBC based dengue detection</p></div>", unsafe_allow_html=True)
