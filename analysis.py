import re, json
from symtomanalys import analysera_symtom

with open("symtomdata.json", encoding="utf-8") as f:
    symtom_dict = json.load(f)

def strukturera_anamnes(text):
    text = text.lower()
    sections = {
        "Age/Sex": "",
        "Presenting complaint (PC)": "",
        "History of presenting complaint (HPC)": "",
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
    for namn, nyckelord in symtom_dict.items():
        if any(w in text for w in nyckelord):
            pc_träffar.append(namn)

    if pc_träffar:
        sections["Presenting complaint (PC)"] = "Patienten uppger:\n- " + "\n- ".join(pc_träffar)

        hpc_resultat = []
        for symtom in pc_träffar:
            analys = analysera_symtom(text, symtom)
            hpc_resultat.append(f"{symtom}:\n- " + "\n- ".join(analys))

        sections["History of presenting complaint (HPC)"] = "\n\n".join(hpc_resultat)

    return sections
