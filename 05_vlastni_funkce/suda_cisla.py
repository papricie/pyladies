# Nejprve si napiš funkci, která rozhodne, jestli zadané číslo je sudé. 
# Funkci si vhodně pojmenuj. Pokud nevíš, jak zjistíš, že dané číslo je sudé, 
# zkus se podívat na operátor modulo % a zamysli se, 
# jak by se dal použít pro vyřešení úkolu.

# Potom napiš funkci, která pro zadaný počet n vygeneruje n náhodných čísel, 
# a každé vygenerované číslo vypíše spolu s informací, jestli je liché nebo sudé. 
# Tuto funkci si pojmenuj jednoduše sudost_nahodnych_cisel(pocet).

# V hlavním kódu programu funkci sudost_nahodnych_cisel zavolej.

import random

def over_sudost(cislo):
    """Funkce vrátí True, pokud je číslo sudé, jinak False."""
    return cislo % 2 == 0



def sudost_nahodnych_cisel(pocet):
    """Funkce vygeneruje zadaný počet náhodných čísel a vypíše jejich sudost."""
    for i in range(pocet):
        cislo = random.randint(1, 100)  
        if over_sudost(cislo):
            print(f"{cislo} je sudé.")
        else:
            print(f"{cislo} je liché.")

sudost_nahodnych_cisel(3) 
