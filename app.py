import streamlit as st

st.set_page_config(page_title="Medical Diagnosis System", layout="wide")

st.markdown("""
<style>
.card {
    background: linear-gradient(145deg, #0f172a, #020617);
    border-radius: 18px;
    padding: 30px;
    height: 220px;
    color: white;
    position: relative;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    transition: transform 0.2s ease;
}
.card:hover {
    transform: scale(1.03);
}
.card-button {
    position: absolute;
    inset: 0;
    opacity: 0;
}
.card-title {
    font-size: 26px;
    font-weight: 700;
}
.card-desc {
    margin-top: 12px;
    font-size: 16px;
    color: #cbd5f5;
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 Intelligent Medical Diagnosis System")
st.write("Click on any disease card to start prediction")

st.markdown("---")

col1, col2, col3 = st.columns(3)

def disease_card(col, title, desc, page):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(" ", key=page):
            st.switch_page(page)

# ---------- ROW 1 ----------
disease_card(col1, "❤️ Heart Disease", "Cardiac risk prediction", "pages/1_Heart_Disease.py")
disease_card(col2, "🫁 Lung Cancer", "Lung cancer risk assessment", "pages/2_Lung_Cancer.py")
disease_card(col3, "🩸 Diabetes", "Blood sugar & diabetes risk", "pages/3_Diabetes.py")

# ---------- ROW 2 ----------
col4, col5, col6 = st.columns(3)

disease_card(col4, "🧠 Kidney Disease", "Kidney function analysis", "pages/4_Kidney_Disease.py")
disease_card(col5, "🦋 Thyroid", "Hormonal disorder detection", "pages/5_Thyroid.py")
disease_card(col6, "🦟 Dengue", "CBC based dengue detection", "pages/6_Dengue.py")
