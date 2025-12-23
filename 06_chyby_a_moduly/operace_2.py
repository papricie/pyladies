# V lekci Funkce a želva jsi napsala program, 
# který postupně načte od uživatele dvě čísla 
# a operaci ('+', '-', '*' nebo '/') 
# a provede na číslech příslušnou operaci.

###########################################################
# Původní kód vypadá takto:

# prvni = float(input("První číslo: "))
# druhe = float(input("Druhé číslo: "))
# operace = input("Operace (+, -, *, /): ")

# if operace == "+":
#     vysledek = prvni + druhe
# elif operace == "-":
#     vysledek = prvni - druhe
# elif operace == "*":
#     vysledek = prvni * druhe
# elif operace == "/":
#     if druhe == 0:
#         raise ValueError("Nelze dělit nulou")
#     vysledek = prvni / druhe
# else:
    # print("Neplatná operace.")
    # quit()

# print(prvni, operace, druhe, "=", vysledek)
###########################################################

# Program uprav tak, aby:
# při špatném vstupu napověděl, co očekává, a zeptal se znovu
# při dělení nulou vypsal hlášku Nulou nelze dělit.
# Použij na to ošetření příslušné chyby (tj. ne if delitel == 0:).

# Příklad použití:
# První číslo: třistatřiatřicet
# Zadávej jen čísla
# První číslo: 333
# Druhé číslo: 0
# Operace: /
# Nulou nelze dělit.

### KOMENTÁŘE K ŘEŠENÍ ###
# ještě v tom jsou mouchy zkus si to projít ;) 
# nápověda: jde 8888 :)

# jak jsem koukl dá tak i ty další řádky 
# od 18 dál by chtěly poladit, Opravě zdar! To dáš! :)
###

while True:
    try:
        prvni = float(input("První číslo: ")) 
        break
    except ValueError:
        print("Zadávej jen čísla")

while True:
    try:
        druhe = float(input("Druhé číslo: "))
        break
    except ValueError:
        print("Zadávej jen čísla")

while True:
    operace = input("Operace (+, -, *, /): ")
    if operace in ("+", "-", "*", "/"):
        break
    else:
        print("Neplatná operace. Zadej jednu z +, -, *, /.")

while True:
    try:
        if operace == "+":
            vysledek = prvni + druhe
        elif operace == "-":
            vysledek = prvni - druhe
        elif operace == "*":
            vysledek = prvni * druhe
        elif operace == "/":
            vysledek = prvni / druhe
        print(prvni, operace, druhe, "=", vysledek)
        break  
    except ZeroDivisionError:
        print("Nulou nelze dělit.")
        druhe = float(input("Zadej jiné druhé číslo: "))

