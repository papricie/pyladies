def vrat_nasobky(cislo):
    """Funkce vrátí prvních deset násobků zadaného čísla."""
    return [cislo * i for i in range(1, 11)]

print(vrat_nasobky(5))
print(vrat_nasobky(10))
print(vrat_nasobky(-3))