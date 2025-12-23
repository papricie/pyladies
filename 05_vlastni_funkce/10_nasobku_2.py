# Změn proceduru z předchozího úkolu tak, 
# aby funkce měla tři argumenty – číslo, počet vypisovaných násobků, 
# znak pro oddělení vypsaných násobků.

###
# skoro, teď se procedura řídí pouze prvními dvěma argumenty. 
# i kdyby jsme jako oddělovač zadali třeba " | ", 
# budou se násobky vypisovat oddělené čárkou, 
# protože se vypisuje jednoduše celý seznam.

# BEZ SEZNAMU by to mělo vypadat nějak takto:

def vypis_nasobky(cislo, pocet_nasobku, oddelovac):
    """Funkce vypíše zadaný počet násobků zadaného čísla a oddělí je."""
    nasobky = []
    for i in range(1, pocet_nasobku + 1): # +1 protože range je do, ale ne včetně
        nasobky.append(str(cislo * i))  # Převod na řetězec pro správné spojení
    print(oddelovac.join(nasobky))  # Spojení pomocí zadaného oddělovače
vypis_nasobky(3, 5, " | ")
# Výstup: 3 | 6 | 9 | 12 | 15
