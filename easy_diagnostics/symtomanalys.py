import re
from easy_diagnostics.smartanalys import analysera_sokrates

def analysera_symtom(text, symtom):
    resultat = []
    if not text:
        return resultat
    resultat.append(f"Karaktär: {symtom}")
    if re.search(r"(intermittent|kommer och går|periodvis)", text):
        resultat.append("Mönster: intermittent")
    elif re.search(r"(ständig|konstant|ihållande|hela tiden)", text):
        resultat.append("Mönster: konstant")
    if re.search(r"(blivit värre|försämrats|tilltagit)", text):
        resultat.append("Förlopp: försämring")
    elif re.search(r"(förbättrats|lindrats|blivit bättre)", text):
        resultat.append("Förlopp: förbättring")
    elif re.search(r"(oförändrad|lika illa|samma som innan)", text):
        resultat.append("Förlopp: oförändrat")
    return resultat
