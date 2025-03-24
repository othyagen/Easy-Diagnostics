import re
from socrates import analysera_socrates

def analysera_symtom(text, symtom_namn):
    text = text.lower()
    analys = []

    analys.append(f"Karaktär: {symtom_namn.lower()}")

    if "plötsligt" in text:
        analys.append("Debut: plötslig")
    elif "gradvis" in text:
        analys.append("Debut: gradvis")

    if re.search(r"(för|sedan)\s+\d+\s+(dagar?|veckor?|timmar?)", text):
        analys.append("Tidsangivelse: " + re.search(r"(för|sedan)\s+\d+\s+(dagar?|veckor?|timmar?)", text).group(0))

    if "haft tidigare" in text:
        analys.append("Tidigare episoder: ja")

    if "konstant" in text:
        analys.append("Mönster: konstant")
    elif "kommer och går" in text or "intermittent" in text:
        analys.append("Mönster: intermittent")

    if "förvärrats" in text or "blivit värre" in text:
        analys.append("Förlopp: försämring")
    elif "förbättrats" in text or "blivit bättre" in text:
        analys.append("Förlopp: förbättring")

    if "förvärras" in text:
        analys.append("Förvärras av: ansträngning")
    if "lindras" in text:
        analys.append("Lindras av: vila")

    associerade = []
    for sym in ["hosta", "illamående", "feber", "yrsel", "trötthet"]:
        if sym in text:
            associerade.append(sym)
    if associerade:
        analys.append("Associerade symtom: " + ", ".join(associerade))

    if "ont" in symtom_namn or "smärta" in symtom_namn:
        socrates = analysera_socrates(text, symtom_namn.split()[-1])
        if socrates:
            analys.append("🩸 SOCRATES:")
            for rad in socrates:
                analys.append("  - " + rad)

    return analys
