# Tyhle funkce už známe. print vypíše nepojmenované argumenty, oddělené mezerou. 
# Pojmenovaný argument end určuje, co se vypíše na konci (místo přechodu na nový řádek); 
# sep udává, co se vypíše mezi jednotlivými argumenty (místo mezery).

print(1, 'dvě', False)
print(1, end=' ')
print(2, 3, 4, sep=', ')
# 1 dvě False
# 1 2, 3, 4


# input vypíše zadaný řetězec (pokud je nějaký) a čeká na vstup od uživatele.
# Když uživatel něco napíše a stiskne Enter, vrátí to, co napsal, jako řetězec.
vstup = input('zadej vstup: ')
#       ╰─────────┬─────────╯
vstup =         'ahoj'
print(vstup)
# zadej vstup:  user types: ahoj
# 'ahoj'   


# Jak Python vyhodnotí tento výraz? Zadá-li uživatel 42Enter, funkce input vrátí řetězec'42'. 
# Ten pak funkce int vezme jako argument, udělá podle něj číslo a to číslo vrátí:

cislo = int(input('Zadej číslo: '))
      #     ╰─────────┬─────────╯
cislo = int(        '42'          )
      # ╰────────────┬────────────╯
cislo =             42
print (cislo)
# cislo má teď hodnotu 42 (jako číslo, ne jako řetězec)






# Matematické funkce
#Jedna zajímavá matematická funkce je k dispozici vždy:

round(cislo)    # zaokrouhlení

from math import sqrt, floor, ceil

sqrt(cislo)     # druhá odmocnina
floor(cislo)    # zaokrouhlení dolů
ceil(cislo)     # zaokrouhlení nahoru

from math import sin, cos, tan, degrees, radians

uhel = 0
sin(uhel)       # sinus
cos(uhel)       # kosinus
tan(uhel)       # tangens

degrees(uhel)   # převod z radiánů na stupně
radians(uhel)   # převod ze stupňů na radiány

#Při importování je potřeba si dávat pozor na pojmenování souborů: 
# importuješ-li from math, nesmí se tvůj program jmenovat math.py.




# Náhoda
from random import randrange, uniform

a = 10
b = 20

randrange(a, b)   # náhodné celé číslo od a do b-1
uniform(a, b)     # náhodné reálné číslo od a do b

#Pozor na to, že randrange(a, b) nikdy nevrátí samotné b. 
# Pokud potřebuješ náhodně vybrat ze tří možností, 
# použij randrange(0, 3), což vrátí 0, 1, nebo 2:

from random import randrange

cislo = randrange(0, 3)  # číslo je 0, 1, nebo 2
if cislo == 0:
    print('Kolečko')
elif cislo == 1:
    print('Čtvereček')
else:  # tady musí být číslo 2
    print('Trojúhelníček')

# Pamatuj, když importuješ z modulu random, nesmí se tvůj soubor jmenovat random.py.



