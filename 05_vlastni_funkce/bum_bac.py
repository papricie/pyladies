# Napiš funkci, která bude mít jako parametr jedno číslo a vrátí "Bum", 
# je-li toto číslo liché, a "Bác", je-li toto číslo sudé.

# Pak napiš funkci, která bude mít jako parametr jedno číslo (n) 
# a vypíše n řádek. Na prvním řádku bude "Bum", na druhém "Bác", 
# na třetím "Bum", atd.

#Např.

# >>> vypis_bum_bac(5)
# Bum
# Bác
# Bum
# Bác
# Bum


def vrat_bum_nebo_bac (cislo):
    """Funkce vrátí 'Bum', pokud je číslo liché, 'Bac', pokud je sudé."""
    if cislo % 2 == 0:
        return "Bac"
    else:
        return "Bum"
#print(vrat_bum_nebo_bac(3))
#print(vrat_bum_nebo_bac(4))

def vrat_bum_bac_cyklem(cislo):
    vysledek = []
    for i in range(1, cislo + 1):
        if i % 2 == 0:
            vysledek.append("Bac")
        else:
            vysledek.append("Bum")
    return vysledek

for radek in vrat_bum_bac_cyklem(7):
    print(radek) 