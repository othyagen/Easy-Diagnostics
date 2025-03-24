import re

def analysera_socrates(text, plats):
    text = text.lower()
    result = []

    if plats in text:
        result.append(f"Plats: {plats}")

    if "plötsligt" in text:
        result.append("Debut: plötslig")
    elif "gradvis" in text:
        result.append("Debut: gradvis")

    if re.search(r"(för|sedan)\s+\d+\s+(dagar?|timmar?)", text):
        result.append("Tidsangivelse: " + re.search(r"(för|sedan)\s+\d+\s+(dagar?|timmar?)", text).group(0))

    for kar in ["tryckande", "dov", "brännande", "huggande"]:
        if kar in text:
            result.append(f"Karaktär: {kar}")
            break

    if "strålar" in text or "ut i" in text:
        if "arm" in text:
            result.append("Utstrålning: ut i armen")
        if "rygg" in text:
            result.append("Utstrålning: mot ryggen")
        if "käke" in text:
            result.append("Utstrålning: mot käken")

    associerade = []
    for sym in ["illamående", "svettningar", "yrsel", "andfådd"]:
        if sym in text:
            associerade.append(sym)
    if associerade:
        result.append("Associerade symtom: " + ", ".join(associerade))

    if "kommer och går" in text:
        result.append("Tidsmönster: intermittent")
    elif "konstant" in text:
        result.append("Tidsmönster: konstant")

    if "förvärras" in text:
        result.append("Förvärras av: ansträngning")
    if "lindras" in text:
        result.append("Lindras av: vila")

    if re.search(r"(\d+)\s+(av|på)\s+10", text):
        result.append("Smärtintensitet: " + re.search(r"(\d+)\s+(av|på)\s+10", text).group(0))

    return result
