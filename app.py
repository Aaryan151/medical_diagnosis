import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis System",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("""
<div style="
    background: linear-gradient(90deg,#b31217,#e52d27);
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 40px;
">
    <h1 style="color:white; margin-bottom:5px;">Medical Diagnosis System</h1>
    <p style="color:#f2f2f2;">Early detection saves lives</p>
</div>
""", unsafe_allow_html=True)

# ---------- CARD STYLE ----------
card_style = """
<style>
.card {
    background: linear-gradient(135deg,#b31217,#e52d27);
    padding: 35px;
    border-radius: 20px;
    color: white;
    height: 170px;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 12px 30px rgba(255,0,0,0.35);
}
.title {
    font-size: 24px;
    font-weight: 600;
}
.subtitle {
    font-size: 15px;
    opacity: 0.9;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# ---------- GRID ----------
row1 = st.columns(3)
row2 = st.columns(3)

# ---------- HEART ----------
with row1[0]:
    if st.button("❤️ Heart Disease", use_container_width=True):
        st.switch_page("pages/1_Heart_Disease.py")
    st.markdown("<div class='card'><div class='title'>Heart Disease</div><div class='subtitle'>Cardiac risk prediction</div></div>", unsafe_allow_html=True)

# ---------- LUNG ----------
with row1[1]:
    if st.button("🫁 Lung Cancer", use_container_width=True):
        st.switch_page("pages/2_Lung_Cancer.py")
    st.markdown("<div class='card'><div class='title'>Lung Cancer</div><div class='subtitle'>Lung cancer risk assessment</div></div>", unsafe_allow_html=True)

# ---------- DIABETES ----------
with row1[2]:
    if st.button("🩸 Diabetes", use_container_width=True):
        st.switch_page("pages/3_Diabetes.py")
    st.markdown("<div class='card'><div class='title'>Diabetes</div><div class='subtitle'>Blood sugar & diabetes risk</div></div>", unsafe_allow_html=True)

# ---------- KIDNEY ----------
with row2[0]:
    if st.button("🧠 Kidney Disease", use_container_width=True):
        st.switch_page("pages/4_Kidney_Disease.py")
    st.markdown("<div class='card'><div class='title'>Kidney Disease</div><div class='subtitle'>Kidney function analysis</div></div>", unsafe_allow_html=True)

# ---------- THYROID ----------
with row2[1]:
    if st.button("🦋 Thyroid", use_container_width=True):
        st.switch_page("pages/5_Thyroid.py")
    st.markdown("<div class='card'><div class='title'>Thyroid</div><div class='subtitle'>Hormonal disorder detection</div></div>", unsafe_allow_html=True)

# ---------- DENGUE ----------
with row2[2]:
    if st.button("🦟 Dengue", use_container_width=True):
        st.switch_page("pages/6_Dengue.py")
    st.markdown("<div class='card'><div class='title'>Dengue</div><div class='subtitle'>CBC based dengue detection</div></div>", unsafe_allow_html=True)
