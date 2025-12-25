# Doplň funkci pohyb tak, aby při pohybu umazala první bod 
# ze seznamu souřadnic. Výsledný seznam tak bude mít stejnou 
# délku jako před voláním.

from mapa import nakresli_mapu

def pohyb(seznam_souradnic, smer):
    """
    Přidá novou souřadnici do seznamu_souradnic
    na základě poslední souřadnice a zadaného směru.
    Také odstraní první souřadnici ze seznamu, aby délka zůstala stejná.
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
    
    seznam_souradnic.pop(0)  # Odstranění první souřadnice ze seznamu

    seznam_souradnic.append(nova_souradnice)  # Přidání nové souřadnice do seznamu

