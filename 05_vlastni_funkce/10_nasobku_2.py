def vrat_nasobky(cislo1, cislo2, cislo3):
    """Funkce vrátí prvních deset násobků zadaných čísel."""
    return [(cislo1 * i, cislo2 * i, cislo3 * i) for i in range(1, 11)]

print(vrat_nasobky(5, 10, -3))