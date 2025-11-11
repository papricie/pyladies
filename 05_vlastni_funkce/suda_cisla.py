import random

def over_sudost(cislo):
    """Funkce vrátí True, pokud je číslo sudé, jinak False."""
    return cislo % 2 == 0

print(over_sudost(4))

def sudost_nahodnych_cisel(pocet):
    """Funkce vygeneruje zadaný počet náhodných čísel a vrátí seznam sudých čísel."""
    seznam_sudych_cisel = []
    for i in range(pocet): # generování zadaného počtu čísel pri volaní funkce
        cislo = random.randint(1, 100)
        if over_sudost(cislo): # použití funkce pro ověření sudosti
            seznam_sudych_cisel.append(cislo) # přidání sudého čísla do seznamu
    return seznam_sudych_cisel
print(sudost_nahodnych_cisel(10))