# Doplň funkci pohyb tak, aby zamezila:

# pohybu ven z mapy,
# pohybu na políčko, které už v seznamu je.
# Vhodná výjimka pro tyto situace je RuntimeError('Game over').

from mapa import nakresli_mapu

def pohyb(seznam_souradnic, smer):
    posledni_souradnice = seznam_souradnic[-1]
    x, y = posledni_souradnice

    # Výpočet nové souřadnice
    if smer == 'w':          # nahoru
        nova_souradnice = (x, y - 1)
    elif smer == 's':        # dolů
        nova_souradnice = (x, y + 1)
    elif smer == 'd':        # vpravo
        nova_souradnice = (x + 1, y)
    elif smer == 'a':        # vlevo
        nova_souradnice = (x - 1, y)
    else:
        raise ValueError("Neplatný směr. Použijte 'w', 's', 'd' nebo 'a'.")

    # Kontrola pohybu ven z mapy
    x_nove, y_nove = nova_souradnice
    if not (0 <= x_nove <= 9 and 0 <= y_nove <= 9):
        raise RuntimeError("Game over")

    # Kontrola obsazeného políčka
    if nova_souradnice in seznam_souradnic:
        raise RuntimeError("Game over")

    # Pohyb hada
    seznam_souradnic.pop(0)
    seznam_souradnic.append(nova_souradnice)
