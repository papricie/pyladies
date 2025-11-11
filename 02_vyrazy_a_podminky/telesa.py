
#Napiš program, který se uživatele zeptá:
#na těleso, které má vypočítat (krychle, koule, kvádr)
#na metriku, kterou má vypočítat (objem, povrch)
#na velikost (délku strany, průměr)
#Program požadovanou metriku spočítá a vypíše výsledek.

# Vyber telesa
teleso = input("Jake teleso pocitame? (krychle, koule, kvadr) ")

if teleso == "krychle":
    print("V poradku.")
elif teleso == "koule":
    print("V poradku.")
elif teleso == "kvadr":
    print("V poradku.")
else:
    print("Neznamy typ telesa.")
    exit()

# Vyber metriky
metrika = input("Jakou metriku pocitame? (objem, povrch) ")

if metrika == "objem":
    print("Vypocitam objem.")
elif metrika == "povrch":
    print("Vypocitam povrch.")
else:
    print("Neznamy typ metriky.")
    exit()

# Zadani velikosti   
velikost = float(input("Delka strany (krychle, kvadr) nebo prumeru (koule) v cm? "))
if velikost <= 0:
    print("Cislo musi byt kladne.")
    exit()
# krychle
if teleso == "krychle":
    if metrika == "objem":
        objem = velikost ** 3
        print("Objem krychle je", objem ,"cm3")
    elif metrika == "povrch":
        povrch = 6 * (velikost ** 2)
        print("Povrch krychle je", povrch ,"cm2")
# koule
elif teleso == "koule":
    if metrika == "objem":
        objem = (4/3) * 3.14 * ((velikost / 2) ** 3)
        print("Objem koule je", objem ,"cm3")
    elif metrika == "povrch":
        povrch = 4 * 3.14 * ((velikost / 2) ** 2)
        print("Povrch koule je", povrch ,"cm2")
# kvadr - zadani dalsich stran
elif teleso == "kvadr":
    strana_b = float(input("Zadej druhou stranu: "))
    if strana_b <= 0:
        print("Cislo musi byt kladne.")
        exit()
    strana_c = float(input("Zadej treti stranu: "))
    if strana_c <= 0:
        print("Cislo musi byt kladne.")
        exit()

    if metrika == "objem":
        objem = velikost * strana_b * strana_c
        print("Objem kvadru je", objem ,"cm3")
    elif metrika == "povrch":
        povrch = 2 * (velikost * strana_b + velikost * strana_c + strana_b * strana_c)
        print("Povrch kvadru je", povrch ,"cm2")
