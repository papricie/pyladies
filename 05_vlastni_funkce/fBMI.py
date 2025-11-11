def vypocitej_fbmi(obvod_hrudniku, delka_nohy):
    """Funkce vypočítá a vrátí hodnotu FBMI podle zadaných parametrů."""
    fbmi = (((obvod_hrudniku / 0.7062) - delka_nohy) / 0.9156) - delka_nohy
    return fbmi

print(vypocitej_fbmi(40, 20))
    