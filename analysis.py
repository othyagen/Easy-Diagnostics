import re
import json
from easy_diagnostics.symtomanalys import analysera_symtom, analysera_sokrates

with open("symtomdata.json", encoding="utf-8") as f:
    symtom_dict = json.load(f)

def extrahera_meningar(text):
    return re.split(r'(?<=[.!?])\s+', text)

def hitta_relevanta_meningar(text, nyckelord_lista):
    meningar = extrahera_meningar(text)
    relevanta = []
    for mening in meningar:
        for nyckelord in nyckelord_lista:
            if nyckelord.lower() in mening.lower():
                relevanta.append(mening.strip())
                break
    return relevanta

def strukturera_anamnes(text):
    text = text.lower()

    sections = {
        "Age/Sex": "",
        "Presenting complaint (PC)": "",
        "History of presenting complaint (HPC)": [],
        "Past medical history (PMH)": "",
        "Drug history (DHx)": "",
        "Allergies/reactions": "",
        "Alcohol": "",
        "Smoking": "",
        "Family history (FHx)": "",
        "Social history (SHx)": "",
        "Systematic enquiry": "",
        "Exam": "",
        "Investigations": "",
    }

    age_sex_match = re.search(r"(\d{1,3})\s*(-| )?(år(ig| gammal)?)?\s*(man|kvinna|pojke|flicka|gosse|tös|jänta|påg)", text)
    if age_sex_match:
        age = age_sex_match.group(1)
        sex_raw = age_sex_match.group(5)
        kön_map = {"gosse": "pojke", "påg": "pojke", "tös": "flicka", "jänta": "flicka"}
        sex = kön_map.get(sex_raw, sex_raw)
        sections["Age/Sex"] = f"{age} år, {sex}"

    pc_träffar = []
    for namn, info in symtom_dict.items():
        nyckelord = info.get("nyckelord", [])
        if any(w in text for w in nyckelord):
            pc_träffar.append(namn)

    if pc_träffar:
        sections["Presenting complaint (PC)"] = "Patienten uppger:\n- " + "\n- ".join(pc_träffar)

        hpc_resultat = []
        for symtom in pc_träffar:
            nyckelord = symtom_dict[symtom].get("nyckelord", [])
            meningar = hitta_relevanta_meningar(text, nyckelord)
            relevant_text = " ".join(meningar)
            if any(s in relevant_text for s in ["ont", "smärta", "molande", "stickande", "brännande", "huggande", "tryckande", "skärande"]):
                analys = analysera_sokrates(relevant_text, symtom)
            else:
                analys = analysera_symtom(relevant_text, symtom)
            if analys:
                hpc_resultat.append(f"🩺 {symtom}")
                hpc_resultat.extend([f"• {rad}" for rad in analys])
                hpc_resultat.append("")
        sections["History of presenting complaint (HPC)"] = hpc_resultat or ["*Ej angivet*"]

    return sections
