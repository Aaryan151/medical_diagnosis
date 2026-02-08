import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis System",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("""
<div style="
    background: linear-gradient(90deg, #b91c1c, #7f1d1d);
    padding: 32px;
    border-radius: 14px;
    color: white;
    text-align: center;
">
    <h1>Medical Diagnosis System</h1>
    <p>Early detection saves lives</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- CARD CSS ----------
st.markdown("""
<style>
.card {
    position: relative;
    background: linear-gradient(135deg, #dc2626, #7f1d1d);
    padding: 30px;
    border-radius: 16px;
    height: 170px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.25);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 22px 45px rgba(0,0,0,0.35);
}
.card h2 {
    margin: 0;
    color: white;
    font-size: 26px;
}
.card p {
    margin-top: 10px;
    color: #fef2f2;
    font-size: 15px;
}
.card a {
    position: absolute;
    inset: 0;
    z-index: 10;
}
</style>
""", unsafe_allow_html=True)

# ---------- ROW 1 ----------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h2>❤️ Heart Disease</h2>
        <p>Cardiac risk prediction</p>
        <a href="/Heart_Disease"></a>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h2>🫁 Lung Cancer</h2>
        <p>Lung cancer risk assessment</p>
        <a href="/Lung_Cancer"></a>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h2>🩸 Diabetes</h2>
        <p>Blood sugar & diabetes risk</p>
        <a href="/Diabetes"></a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- ROW 2 ----------
c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""
    <div class="card">
        <h2>🧠 Kidney Disease</h2>
        <p>Kidney function analysis</p>
        <a href="/Kidney_Disease"></a>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="card">
        <h2>🦋 Thyroid</h2>
        <p>Hormonal disorder detection</p>
        <a href="/Thyroid"></a>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="card">
        <h2>🦟 Dengue</h2>
        <p>CBC based dengue detection</p>
        <a href="/Dengue"></a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:gray;'>Powered by AI | Medical & Educational Assistance</p>",
    unsafe_allow_html=True
)
