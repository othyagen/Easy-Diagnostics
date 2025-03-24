# 🩺 Medicinsk App – Steg 1

Detta är en Streamlit-baserad prototyp för att strukturera anamnes från fritext på svenska.

---

## ✅ Funktioner hittills

### 📥 Inmatning
- Ett stort textfält där användaren kan klistra in eller skriva en fri sjukhistoria.

---

### 🧠 Automatisk strukturering
Texten analyseras och delas upp i följande sektioner:

1. **Age/Sex** – tolkar ålder och kön (även dialektala uttryck som "jänta", "påg")
2. **Presenting complaint (PC)** – extraherar huvudsymtom från fritext (dyspné, buksmärta etc.)
3. **History of presenting complaint (HPC)** – analyserar varje PC individuellt:
   - 🔎 Identifierar relaterade meningar
   - 🧱 Använder ett gemensamt analysramverk:
     - Vanliga symtom → `symtomanalys.py`
     - Smärta → `SOKRATES-modellen` (plats, karaktär, förlopp, strålning etc.)
     - Smärta aktiveras både av ord som "ont" och beskrivningar som "molande", "stickande", "brännande" osv.
4. **Past medical history (PMH)**
5. **Drug history (DHx)**
6. **Allergies/reactions**
7. **Alcohol**
8. **Smoking**
9. **Family history (FHx)**
10. **Social history (SHx)**
11. **Systematic enquiry**
12. **Exam**
13. **Investigations**

---

### 📋 Visning
- Varje sektion presenteras med **fet rubrik**
- HPC visar varje symtom tydligt med:
  ```
  🩺 Dyspné
  • Karaktär: dyspné
  • Mönster: konstant
  ```
- Särskild formattering för läsbarhet

---

### 🔍 Utforska & redigera symtom
- Visning av alla kända symtom från `symtomdata.json`
- Sökfält, filter per system, lokalisation och alarmsymtom
- Möjlighet att redigera eller lägga till egna symtom
- Tydligt redigeringsläge med indikator

---

## 📦 Filer
- `app.py` – huvudgränssnitt för användaren
- `analysis.py` – innehåller logik för att strukturera texten
- `symtomanalys.py` – analyslogik för symtom och smärta
- `symtomdata.json` – lista med alla kända symtom och metadata

---

## 🔜 Nästa steg (förslag)
- Steg 2: Diagnosförslag
- Steg 3: Handläggningsrekommendationer
- Export till PDF/JSON
- AI-baserad prioritering av symtom
