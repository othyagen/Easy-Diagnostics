import streamlit as st
import json
from easy_diagnostics.analysis import strukturera_anamnes

SYMPTOM_FILE = "symtomdata.json"

def load_symptom_data():
    with open(SYMPTOM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_symptom_data(data):
    with open(SYMPTOM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

st.set_page_config(page_title="Medicinsk app", layout="wide")
view = st.sidebar.radio("Välj vy:", ["📋 Strukturerad anamnes", "🔍 Utforska & redigera symtom"])

if view == "📋 Strukturerad anamnes":
    st.title("🩺 Medicinsk app – Steg 1")
    input_text = st.text_area("Inmatning (kontinuerlig text)", height=300)
    if input_text:
        strukturerad = strukturera_anamnes(input_text)
        st.subheader("📋 Strukturerad anamnes:")
        for rubrik, innehåll in strukturerad.items():
            st.markdown(f"\n**{rubrik}:**")
            if rubrik == "History of presenting complaint (HPC)":
                for rad in innehåll:
                    st.markdown(rad)
            else:
                st.markdown(innehåll if innehåll else "*Ej angivet*")
