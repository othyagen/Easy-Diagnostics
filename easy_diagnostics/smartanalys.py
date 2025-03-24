import re

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
