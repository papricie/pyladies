# Vytvoř funkci, která spočítá Body Mass Index pro kočky. 
# Vstupem (parametry) funkce bude obvod hrudníku (cm) 
# a délka zadní nohy od kolena ke kotníku (cm). F
# unkce vrátí číslo feline body mass index (fBMI).

# Postup výpočtu fBMI:
# Obvod hrudníku vyděl číslem 0.7062 a odečti délku nohy.
# Výsledek vyděl číslem 0.9156.
# Od výsledku z bodu 2 odečti délku nohy.

# Napiš funkci, která na základě hodnoty fBMI rozhodne, 
# jaká kočka je. Čtyři kategorie vychrtlosti nebo sádelnatosti 
# kočky jsou určeny hranicemi 15, 30, a 42. 
# Funkce vrátí textový popis stavu kočky, například 
# 'podvyživená', 'zdravá', 'tlustá', 'jako kopačák'. 
# Použij fantazii a třeba i přidej několik kategorií.

# Funkce a jejich parametry vhodně pojmenuj.

# Napiš hlavní kód programu, který se uživatele zeptá 
# na parametry kočky a vypíše, jaká kočka je.

def spocitej_fBMI(obvod_hrudniku, delka_nohy):
    """Funkce spočítá fBMI pro kočky podle zadaných parametrů."""
    krok1 = obvod_hrudniku / 0.7062 - delka_nohy
    krok2 = krok1 / 0.9156
    fBMI = krok2 - delka_nohy
    return fBMI
    
def urci_stav_kocky(fBMI):
    """Funkce určí stav kočky na základě hodnoty fBMI."""
    if fBMI < 15:
        return "podvyživená"
    elif 15 <= fBMI < 30:
        return "zdravá"
    elif 30 <= fBMI < 42:
        return "tlustá"
    else:
        return "jako kopačák"


obvod = float(input("Zadej obvod hrudníku kočky (cm): "))
delka = float(input("Zadej délku zadní nohy kočky od kolena ke kotníku (cm): "))

fBMI_hodnota = spocitej_fBMI(obvod, delka)
stav_kocky = urci_stav_kocky(fBMI_hodnota)

print(f"Kočka je {stav_kocky} má fBMI {fBMI_hodnota}")
