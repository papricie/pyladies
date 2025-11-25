# knp.py -- importovatelný modul

import random  # (příp. import jiných věci, které budou potřeba)

def hrej_hru():
    tah_pocitace = 'kámen'
    tah_hrace = input('Co chceš hrát (kámen, nůžky, papír)? ')

    # (tady reálně bude spousta zanořených ifů)
    if tah_hrace == 'papír':
        print('Vyhrála jsi!')
    else:
        print('Nevyhrála jsi...')