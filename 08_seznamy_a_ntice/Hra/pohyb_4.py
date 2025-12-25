
# Pak přidej do hry hadí potravu.
# Seznam jídla obsahuje na začátku dvě jídla na políčkách, 
# na kterých není had (například: jidlo = [(2, 3), (4, 5)] 
# znamená jedno jídlo na pozici (2, 3) a druhé na (4, 5)). 
# Když had sežere jídlo, vyroste („nesmaže“ se mu ocas, 
# tedy neprovede se to, co jsi přidala v předminulém úkolu) 
# a na náhodném prázdném místě se přidá jídlo nové.

# Na mapě se jídlo zobrazuje třeba jako otazník (?).

from mapa import nakresli_mapu
import random

def pohyb(seznam_souradnic, smer, jidlo): # přidán parametr jidlo
    posledni_souradnice = seznam_souradnic[-1]
    x, y = posledni_souradnice

    # Výpočet nové souřadnice
    if smer == 'w':     # nahoru
        nova_souradnice = (x, y - 1)
    elif smer == 's':   # dolů
        nova_souradnice = (x, y + 1)
    elif smer == 'd':   # vpravo
        nova_souradnice = (x + 1, y)
    elif smer == 'a':   # vlevo
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

    # Kontrola jídla
    snedl_jidlo = False
    
    if nova_souradnice in jidlo:
        jidlo.remove(nova_souradnice)
        snedl_jidlo = True

        while True:
            nove_jidlo = (random.randint(0, 9), random.randint(0, 9))
            if nove_jidlo not in seznam_souradnic and nove_jidlo not in jidlo:
                jidlo.append(nove_jidlo)
                break

    # Pohyb hada
    if not snedl_jidlo: # pokud nesnědl jídlo, smaž ocas
        seznam_souradnic.pop(0)

    seznam_souradnic.append(nova_souradnice)
