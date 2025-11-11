def vrat_bum_nebo_bac (cislo):
    """Funkce vrátí 'Bum', pokud je číslo liché, 'Bac', pokud je sudé."""
    if cislo % 2 == 0:
        return "Bac"
    else:
        return "Bum"
print(vrat_bum_nebo_bac(3))

def vrat_bum_bac_cyklem(cislo):
    """Funkce vrátí seznam 'Bum' a 'Bac' v řádcích pod sebou v hodnotě zadaného čísla."""
    vysledek = []
    for i in range(1, cislo + 1):
        if i % 2 == 0:
            vysledek.append("Bac")
        else:
            vysledek.append("Bum")
    return "\n".join(vysledek)

print(vrat_bum_bac_cyklem(7))

