# Vytvoř program, který dělá následující:
# Vybere náhodné číslo ze tří možností (0, 1, nebo 2). (Koukni na předchozí úkol!)
# Je-li číslo 0:
# do proměnné tvar uloží slovo 'trojúhelník';
# jinak, je-li číslo 1:
# do proměnné tvar uloží slovo 'čtverec';
# jinak: 
# do proměnné tvar uloží slovo 'kolečko'.
# Vypíše tvar.

from random import randrange
cislo = randrange(3)
#print(cislo)

if cislo == 0:
    print("trojuhelnik")
elif cislo == 1:
    print("ctverec")
else:
    print("kolecko")