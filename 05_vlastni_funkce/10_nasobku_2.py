# Změn proceduru z předchozího úkolu tak, 
# aby funkce měla tři argumenty – číslo, počet vypisovaných násobků, 
# znak pro oddělení vypsaných násobků.

def vypis_nasobky(cislo, pocet_nasobku, oddelovac):
    """Funkce vypíše zadaný počet násobků zadaného čísla a oddělí je."""
    nasobky = []
    for i in range(1, pocet_nasobku + 1): # +1 protože range je do, ale ne včetně
        nasobky.append(cislo * i)
    print(nasobky)

vypis_nasobky(2, 5, ", ")