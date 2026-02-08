import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis System",
    layout="wide"
)

st.title("🩺 Intelligent Medical Diagnosis System")
st.write("Click on a disease to start prediction")
st.markdown("---")

# ---------- CARD STYLE ----------
CARD_STYLE = """
<style>
.card {
    background-color: #111827;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,0,0,0.4);
    text-align: center;
    height: 200px;
}
.card h3 {
    color: white;
}
.card p {
    color: #9CA3AF;
}
</style>
"""
st.markdown(CARD_STYLE, unsafe_allow_html=True)

# ---------- GRID ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>❤️ Heart Disease</h3>
        <p>Cardiac risk prediction</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Heart Disease"):
        st.switch_page("pages/1_Heart_Disease.py")

with col2:
    st.markdown("""
    <div class="card">
        <h3>🫁 Lung Cancer</h3>
        <p>Lung cancer risk assessment</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Lung Cancer"):
        st.switch_page("pages/2_Lung_Cancer.py")

with col3:
    st.markdown("""
    <div class="card">
        <h3>🩸 Diabetes</h3>
        <p>Blood sugar & diabetes risk</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Diabetes"):
        st.switch_page("pages/3_Diabetes.py")

st.markdown("")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <h3>🧠 Kidney Disease</h3>
        <p>Kidney function analysis</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Kidney Disease"):
        st.switch_page("pages/4_Kidney_Disease.py")

with col5:
    st.markdown("""
    <div class="card">
        <h3>🦋 Thyroid</h3>
        <p>Hormonal disorder detection</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Thyroid"):
        st.switch_page("pages/5_Thyroid.py")

with col6:
    st.markdown("""
    <div class="card">
        <h3>🦟 Dengue</h3>
        <p>CBC based dengue detection</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Dengue"):
        st.switch_page("pages/6_Dengue.py")
