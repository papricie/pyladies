# Napiš proceduru, která vypíše obsah slovníku 
# (klíče a k nim náležící hodnoty) na jednotlivé řádky.

# Například vypis_slovnik(mocniny(4)) vypíše
# Klíč 1, hodnota 1
# Klíč 2, hodnota 4
# Klíč 3, hodnota 9
# Klíč 4, hodnota 16

from A_mocniny import mocniny

def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():  # iterace přes klíče a hodnoty ve slovníku
        print(f"Klíč {klic}, hodnota {hodnota}")  # výpis klíče a hodnoty

vypis_slovnik(mocniny(4)) 