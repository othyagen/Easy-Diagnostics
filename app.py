import streamlit as st
import json
from analysis import strukturera_anamnes

SYMPTOM_FILE = "symtomdata.json"

def load_symptom_data():
    with open(SYMPTOM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_symptom_data(data):
    with open(SYMPTOM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

st.set_page_config(page_title="Medicinsk app", layout="wide")
view = st.sidebar.radio("Välj vy:", ["📋 Strukturerad anamnes", "🛠 Redigera symtomlista"])

if view == "📋 Strukturerad anamnes":
    st.title("🩺 Medicinsk app – Steg 1")
    input_text = st.text_area("Inmatning (kontinuerlig text)", height=300)
    if input_text:
        strukturerad = strukturera_anamnes(input_text)
        st.subheader("📋 Strukturerad anamnes:")
        for rubrik, innehåll in strukturerad.items():
            st.markdown(f"**{rubrik}:**\n{innehåll if innehåll else '*Ej angivet*'}")

elif view == "🛠 Redigera symtomlista":
    st.title("🛠 Redigera symtomlista")
    data = load_symptom_data()

    st.markdown("### Filtrera symtom")
    system_filter = st.selectbox("Filtrera efter system", ["Alla"] + sorted(set(v["system"] for v in data.values())))
    lokalisation_filter = st.selectbox("Filtrera efter lokalisation", ["Alla"] + sorted(set(v["lokalisation"] for v in data.values())))
    alarmsymtom_only = st.checkbox("Visa endast alarmsymtom")

    keys_to_delete = []

    for symtom, info in data.items():
        if (system_filter != "Alla" and info["system"] != system_filter):
            continue
        if (lokalisation_filter != "Alla" and info["lokalisation"] != lokalisation_filter):
            continue
        if alarmsymtom_only and not info.get("alarmsymtom"):
            continue

        with st.expander(symtom):
            new_symtom = st.text_input("Namn", value=symtom, key=symtom)
            new_keywords = st.text_area("Nyckelord (separeras med semikolon)", value="; ".join(info["nyckelord"]), key=symtom+"_kw")
            new_system = st.text_input("System", value=info.get("system", ""), key=symtom+"_sys")
            new_lokal = st.text_input("Lokalisation", value=info.get("lokalisation", ""), key=symtom+"_lok")
            new_alarm = st.checkbox("Alarmsymtom", value=info.get("alarmsymtom", False), key=symtom+"_alarm")

            if new_symtom != symtom:
                data[new_symtom] = data.pop(symtom)
                symtom = new_symtom
            data[symtom] = {
                "nyckelord": [k.strip() for k in new_keywords.split(";")],
                "system": new_system,
                "lokalisation": new_lokal,
                "alarmsymtom": new_alarm
            }

            if st.button(f"❌ Ta bort '{symtom}'", key=symtom+"_del"):
                keys_to_delete.append(symtom)

    for k in keys_to_delete:
        del data[k]

    st.markdown("### Lägg till nytt symtom")
    new_name = st.text_input("Nytt symtomnamn (medicinsk term)", key="new_symtom")
    new_words = st.text_input("Nyckelord (separeras med semikolon)", key="new_keywords")
    new_sys = st.text_input("System", key="new_sys")
    new_lok = st.text_input("Lokalisation", key="new_lok")
    new_alarm = st.checkbox("Alarmsymtom", key="new_alarm")

    if st.button("➕ Lägg till symtom"):
        if new_name and new_words:
            data[new_name] = {
                "nyckelord": [k.strip() for k in new_words.split(";")],
                "system": new_sys,
                "lokalisation": new_lok,
                "alarmsymtom": new_alarm
            }

    if st.button("💾 Spara ändringar"):
        save_symptom_data(data)
        st.success("Symtomdata uppdaterat!")
