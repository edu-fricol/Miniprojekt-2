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
        with open(filnamn, "r", encoding="utf-8") as fil:
            highscore_lista = json.load(fil)
            return highscore_lista
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def spara_highscore(highscore_lista, filnamn="highscore.json"):
    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(highscore_lista, fil, indent=4, ensure_ascii=False)


# === SPELMECKANIK ===

def spela_omgang():

    print(" ")
    print("\n=== SVÅRIGHETSGRADER ===")
    print("\nVälj svårighetsgrad:")
    print("1. Lätt (1-50)")
    print("2. Måttlig (1-100)")
    print("3. Svår (1-200)")
    val = input("Ange svårighetsgrad (1-3): ")

    if val == "1":
        max_tal = 50
    elif val == "2":
        max_tal = 100
    elif val == "3":
        max_tal = 200
    else:
        print("Ogiltigt val. Välj 1, 2 eller 3.")
        return

    hemligt_tal = random.randint(1, max_tal)
    gissningar = 0

    print(" ")
    print("\n=== NY OMGÅNG ===")
    print("Välkommen till Högt/lågt-spelet!")
    print(f"\nJag har valt ett tal mellan 1 och {max_tal}. Kan du gissa det?")

    while True:
        try:
            gissning = int(input("Skriv din gissning: "))
        except ValueError:
            print("Ogiltig inmatning. Vänligen skriv ett heltal.")
            continue

        gissningar += 1

        skillnad = abs(gissning - hemligt_tal)
        if skillnad < 5 and gissning != hemligt_tal:
            print("Du är nära!")
        
        if gissning < hemligt_tal:
            print("För lågt! Försök igen.")
        elif gissning > hemligt_tal:
            print("För högt! Försök igen.")
        else:
            print(f"Grattis! Du gissade rätt på {gissningar} gissningar.")
            return gissningar


# === HIGHSCORE-VISNING ===

def visa_highscore(highscore_lista):

    if not highscore_lista:
        print("Ingen highscore än. Spela en omgång för att skapa en!")
        return
    sorted_highscore = sorted(highscore_lista, key=lambda x: x["gissningar"])
    print("\n=== TOPP 5 ===")
    for i, spelare in enumerate(sorted_highscore[:5], start=1):
        print(f"{i}. {spelare['namn']}: {spelare['gissningar']} gissningar")
    
    snitt = sum(entry["gissningar"] for entry in highscore_lista) / len(highscore_lista)
    print(f"\nGenomsnittliga gissningar: {snitt:.2f}")

# === HUVUDPROGRAM ===

def huvudprogram():

    highscore_lista = ladda_highscore()

    while True:
        print("\n=== MENY ===")
        print("1. Spela ny omgång")
        print("2. Visa highscore")
        print("3. Avsluta")

        val = input("Välj ett alternativ (1-3): ")

        if val == "1":
            gissningar = spela_omgang()
            namn = input("Ange ditt namn för highscore: ")
            highscore_lista.append({"namn": namn, "gissningar": gissningar})
            highscore_lista = sorted(highscore_lista, key=lambda x: x["gissningar"])[:10]
            spara_highscore(highscore_lista)
            igen = input("Vill du spela igen? (j/n): ")
            if igen.lower() != "j":
                print("Tack för att du spelade! Hej då!")
                break



        elif val == "2":
            visa_highscore(highscore_lista)

        elif val == "3":
            print("Tack för att du spelade! Hej då!")
            break

        else:
            print("Ogiltigt val. Vänligen välj 1, 2 eller 3.")


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()
