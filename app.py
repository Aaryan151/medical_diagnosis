import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis System",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("""
<div style="
    background: linear-gradient(90deg, #b91c1c, #7f1d1d);
    padding: 30px;
    border-radius: 12px;
    color: white;
    text-align: center;
">
    <h1>Medical Diagnosis System</h1>
    <p>Early detection saves lives</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- CARD STYLE ----------
st.markdown("""
<style>
.card {
    background: #fff5f5;
    border-top: 6px solid #dc2626;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.12);
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 35px rgba(0,0,0,0.25);
}
.card h2 {
    margin: 0;
    color: #7f1d1d;
}
.card p {
    margin-top: 8px;
    color: #374151;
}
</style>
""", unsafe_allow_html=True)

# ---------- ROW 1 ----------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/1_Heart_Disease.py", label="❤️ Heart Disease")
    st.markdown("<p>Predict risk of heart-related diseases</p></div>", unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/2_Lung_Cancer.py", label="🫁 Lung Cancer")
    st.markdown("<p>Analyze lung cancer risk factors</p></div>", unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/3_Diabetes.py", label="🩸 Diabetes")
    st.markdown("<p>Check diabetes probability</p></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- ROW 2 ----------
c4, c5, c6 = st.columns(3)

with c4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/4_Kidney_Disease.py", label="🧠 Kidney Disease")
    st.markdown("<p>Detect kidney health issues</p></div>", unsafe_allow_html=True)

with c5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/5_Thyroid.py", label="🦋 Thyroid")
    st.markdown("<p>Thyroid level analysis</p></div>", unsafe_allow_html=True)

with c6:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.page_link("pages/6_Dengue.py", label="🦟 Dengue")
    st.markdown("<p>CBC based dengue detection</p></div>", unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:gray;'>Powered by AI | Medical & Educational Assistance</p>",
    unsafe_allow_html=True
)
