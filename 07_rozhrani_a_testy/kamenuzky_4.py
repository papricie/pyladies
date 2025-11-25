# knp.py -- importovatelný modul

import random  # (příp. import jiných věci, které budou potřeba)

def vyhodnot(tah_pocitace, tah_hrace):
    # (tady reálně bude spousta zanořených ifů)
    if tah_hrace == 'papír':
        return 'Vyhrála jsi!'
    else:
        return 'Nevyhrála jsi...'


def hrej_hru():
    tah_pocitace = 'kámen'
    tah_hrace = input('Kam chceš hrát?')

    vysledek = vyhodnot(tah_pocitace, tah_hrace)
    print(vysledek)