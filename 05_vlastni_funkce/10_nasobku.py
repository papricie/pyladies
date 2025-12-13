# Napiš proceduru, která vypíše do jednoho řádku prvních 10 násobků 
# zvoleného čísla (argument funkce). Např.: pro vstup 2 vypíše 
# funkce 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.

def vypis_nasobky(cislo):
    """Funkce vypíše prvních deset násobků zadaného čísla."""
    nasobky = []
    for i in range(1, 11):
        nasobky.append(cislo * i)
    print(nasobky)

vypis_nasobky(2)

