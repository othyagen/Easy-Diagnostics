import re

def analysera_symtom(text, symtom):
    resultat = []
    if not text:
        return resultat

    # Karaktär
    resultat.append(f"Karaktär: {symtom}")

    # Periodicitet/mönster
    if re.search(r"(intermittent|kommer och går|periodvis)", text):
        resultat.append("Mönster: intermittent")
    elif re.search(r"(ständig|konstant|ihållande|hela tiden)", text):
        resultat.append("Mönster: konstant")

    # Förlopp
    if re.search(r"(blivit värre|försämrats|tilltagit)", text):
        resultat.append("Förlopp: försämring")
    elif re.search(r"(förbättrats|lindrats|blivit bättre)", text):
        resultat.append("Förlopp: förbättring")
    elif re.search(r"(oförändrad|lika illa|samma som innan)", text):
        resultat.append("Förlopp: oförändrat")

    # Debut
    if re.search(r"(började|debuterade|sedan i|i \w+sdags|för \d+ dagar)", text):
        resultat.append("Tidsaspekt: " + re.findall(r"(började.*?|sedan i \w+sdags|för \d+ dagar)", text)[0])

    # Associerade symtom
    if re.search(r"(feber|illamående|frossa|kräkning|hosta)", text):
        assoc = re.findall(r"(feber|illamående|frossa|kräkning|hosta)", text)
        resultat.append(f"Associerade symtom: {', '.join(set(assoc))}")

    # Förvärrande faktorer
    if re.search(r"(vid ansträngning|rörelse|hosta|djupandning)", text):
        resultat.append("Förvärras av: ansträngning/rörelse")

    return resultat

def analysera_sokrates(text, symtom):
    resultat = []

    resultat.append(f"Karaktär: {symtom}")

    if match := re.search(r"(på|i|över|bakom) [a-zåäö\s]+", text):
        resultat.append(f"Plats: {match.group()}")

    if re.search(r"(plötsligt|gradvis|började)", text):
        resultat.append("Debut: " + re.findall(r"(plötsligt|gradvis|började)", text)[0])

    if re.search(r"(molande|stickande|brännande|tryckande|huggande|skärande)", text):
        typ = re.findall(r"(molande|stickande|brännande|tryckande|huggande|skärande)", text)[0]
        resultat.append(f"Smärtkaraktär: {typ}")

    if re.search(r"(strålar|sprider sig|ut i)", text):
        resultat.append("Radiation: förekommer")

    if re.search(r"(feber|illamående|andnöd|kräkning)", text):
        assoc = re.findall(r"(feber|illamående|andnöd|kräkning)", text)
        resultat.append(f"Associerade symtom: {', '.join(set(assoc))}")

    if re.search(r"(förvärras|värre vid)", text):
        resultat.append("Förvärrande faktorer: angivna")

    if re.search(r"(lindras av|hjälper med)", text):
        resultat.append("Lindrande faktorer: angivna")

    if match := re.search(r"\b(\d|10)\/10\b", text):
        resultat.append(f"Smärtintensitet: {match.group()}")

    return resultat
