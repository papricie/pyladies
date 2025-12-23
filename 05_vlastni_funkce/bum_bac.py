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

###
# Tady není nutné používat seznam. Zadání je 
# Pak napiš funkci, která bude mít jako parametr 
# jedno číslo (n) a vypíše n řádek. Na prvním 
# řádku bude "Bum", na druhém "Bác", na třetím "Bum", atd.


def vrat_bum_nebo_bac (cislo):
    """Funkce vrátí 'Bum', pokud je číslo liché, 'Bac', pokud je sudé."""
    if cislo % 2 == 0:
        return "Bac"
    else:
        return "Bum"
#print(vrat_bum_nebo_bac(3))
#print(vrat_bum_nebo_bac(4))

def vypis_bum_bac_cyklem(cislo):
    """Funkce vypíše n řádků s Bum a Bac."""
    for i in range(1, cislo + 1):
        print(vrat_bum_nebo_bac(i))

vypis_bum_bac_cyklem(5)

