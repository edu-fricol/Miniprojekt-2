"""
Projekt 2: Högt/lågt-spel med highscore
Ett spel där användaren gissar ett slumpmässigt tal.
Highscore sparas i JSON-format.
"""

import random
import json

# === FILHANTERING ===

def ladda_highscore(filnamn="highscore.json"):
    try:
        with open("highscore.json", "r", encoding="utf-8") as fil:
            highscore_lista = json.load(fil)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def spara_highscore(highscore_lista, filnamn="highscore.json"):
    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(highscore_lista, fil, indent=4, ensure_ascii=False)


# === SPELMECKANIK ===

def spela_omgang():
    """
    Spelar en omgång av Högt/lågt.
    
    Returnerar:
        int: Antalet gissningar som behövdes för att gissa rätt
    """
    # TODO: Implementera funktionen
    # 1. Välj ett slumpmässigt tal mellan 1 och 100 med random.randint()
    # 2. Skapa en variabel för antal gissningar (börja på 0)
    # 3. Skapa en while-loop som fortsätter tills spelaren gissar rätt
    # 4. Inuti loopen: fråga efter gissning, öka räknaren, ge feedback (högt/lågt/rätt)
    # 5. När spelaren gissar rätt: returnera antalet gissningar
    pass


# === HIGHSCORE-VISNING ===

def visa_highscore(highscore_lista):
    """
    Visar highscore-listan sorterad med bästa spelaren först.
    
    Parametrar:
        highscore_lista (list): Listan som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Kontrollera om listan är tom först
    # Tips: Sortera med sorted() och key=lambda x: x["gissningar"]
    # Tips: Använd enumerate() för att numrera spelarna från 1
    pass


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Implementera huvudprogrammet
    # 1. Ladda highscore med ladda_highscore()
    # 2. Skapa en while-loop som visar menyn
    # 3. Menyn ska ha alternativen:
    #    1. Spela ny omgång
    #    2. Visa highscore
    #    3. Avsluta
    # 4. Vid val 1:
    #    - Anropa spela_omgang() för att få antalet gissningar
    #    - Fråga efter spelarens namn
    #    - Skapa en dictionary {"namn": namn, "gissningar": antal}
    #    - Lägg till i highscore-listan
    #    - Spara med spara_highscore()
    # 5. Vid val 2: anropa visa_highscore()
    # 6. Vid val 3: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()