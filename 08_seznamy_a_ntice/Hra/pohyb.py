# Napiš funkci pohyb, která dostane seznam souřadnic 
# a světovou stranu ("s", "j", "v" nebo "z"), 
# a přidá k seznamu poslední bod „posunutý“ v daném směru. 

# Např.:
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

from mapa import nakresli_mapu

def pohyb(seznam_souradnic, smer):
    """
    Přidá novou souřadnici do seznamu_souradnic
    na základě poslední souřadnice a zadaného směru.
    """
    posledni_souradnice = seznam_souradnic[-1]  # Získání poslední souřadnice
    x, y = posledni_souradnice  # Rozdělení na x a y

    if smer == 's':  # směr sever
        nova_souradnice = (x, y - 1)
    elif smer == 'j':  # směr jih
        nova_souradnice = (x, y + 1)
    elif smer == 'v':  # směr východ
        nova_souradnice = (x + 1, y)
    elif smer == 'z':  # směr západ
        nova_souradnice = (x - 1, y)
    else:
        raise ValueError("Neplatný směr. Použijte 's', 'j', 'v' nebo 'z'.")

    seznam_souradnic.append(nova_souradnice)  # Přidání nové souřadnice do seznamu

# Testování funkce pohyb
# seznam_souradnic = [(0, 0)]
# pohyb(seznam_souradnic, 'j')
# print(seznam_souradnic)         # → [(0, 0), (1, 0)]
# pohyb(seznam_souradnic, 'j')
# print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(seznam_souradnic, 'v')
# print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(seznam_souradnic, 'z')
# print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
# print(nakresli_mapu(seznam_souradnic))