import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis System",
    layout="wide"
)

st.title("🩺 Intelligent Medical Diagnosis System")
st.write("Click on a disease to start prediction")
st.markdown("---")

# ---------- STYLE ----------
st.markdown("""
<style>
.card {
    background-color: #0f172a;
    padding: 30px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 0 15px rgba(0,0,0,0.5);
    height: 200px;
}
.card h3 {
    color: white;
}
.card p {
    color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ---------- GRID ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>❤️ Heart Disease</h3>
        <p>Cardiac risk prediction</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Heart Disease", key="heart"):
        st.switch_page("pages/1_Heart_Disease.py")

with col2:
    st.markdown("""
    <div class="card">
        <h3>🫁 Lung Cancer</h3>
        <p>Lung cancer risk assessment</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Lung Cancer", key="lung"):
        st.switch_page("pages/2_Lung_Cancer.py")

with col3:
    st.markdown("""
    <div class="card">
        <h3>🩸 Diabetes</h3>
        <p>Blood sugar & diabetes risk</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Diabetes", key="diabetes"):
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
    if st.button("Open Kidney Disease", key="kidney"):
        st.switch_page("pages/4_Kidney_Disease.py")

with col5:
    st.markdown("""
    <div class="card">
        <h3>🦋 Thyroid</h3>
        <p>Hormonal disorder detection</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Thyroid", key="thyroid"):
        st.switch_page("pages/5_Thyroid.py")

with col6:
    st.markdown("""
    <div class="card">
        <h3>🦟 Dengue</h3>
        <p>CBC based dengue detection</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Dengue", key="dengue"):
        st.switch_page("pages/6_Dengue.py")
