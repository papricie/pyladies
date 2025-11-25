import random  # (příp. import jiných věcí, které budou potřeba)

tah_pocitace = 'kámen'
tah_hrace = input('Co chceš hrát (kámen, nůžky, papír)? ')

# (tady reálně bude spousta zanořených ifů)
if tah_hrace == 'papír':
    print('Vyhrála jsi!')
else:
    print('Nevyhrála jsi...')