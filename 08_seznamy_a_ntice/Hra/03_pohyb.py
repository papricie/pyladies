# Napiš funkci pohyb, která dostane seznam souřadnic 
# a světovou stranu ("s", "j", "v" nebo "z"), 
# a přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:

# seznam_souradnic = [(0, 0)]
# pohyb(seznam_souradnic, 'j')
# print(seznam_souradnic)         # → [(0, 0), (1, 0)]
# pohyb(seznam_souradnic, 'j')
# print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(seznam_souradnic, 'v')
# print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(seznam_souradnic, 'z')
# print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
# Funkce nic nevrací. Jen mění už existující seznam.

from mapa.py import nakresli_mapu

def pohyb(seznam_souradnic, smer):
    """
    Přidá do seznamu_souradnic novou pozici na základě směru pohybu.
    """
    posledni_pozice = seznam_souradnic[-1]  # Získání poslední pozice
    x, y = posledni_pozice  # Rozdělení na souřadnice x a y

    if smer == 's':  # sever
        nova_pozice = [(0, 0), (1, 0)]
    elif smer == 'j':  # jih
        nova_pozice = (x, y + 1)
    elif smer == 'v':  # východ
        nova_pozice = (x + 1, y)
    elif smer == 'z':  # západ
        nova_pozice = (x - 1, y)
    else:
        raise ValueError("Neplatný směr. Použijte 's', 'j', 'v' nebo 'z'.")

    seznam_souradnic.append(nova_pozice)  # Přidání nové pozice do seznamu