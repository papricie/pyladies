
#Napiš program, který se uživatele zeptá:
#na těleso, které má vypočítat (krychle, koule, kvádr)
#na metriku, kterou má vypočítat (objem, povrch)
#na velikost (délku strany, průměr)
#Program požadovanou metriku spočítá a vypíše výsledek.


teleso = input("Jake teleso pocitame? (krychle, koule,kvadr) ")

if teleso == "krychle":
    print("V poradku.")
elif teleso == "koule":
    print("V poradku.")
elif teleso == "kvadr":
    print("V poradku.")
else:
    print("Neznamy typ telesa.")
    quit()

metrika = input("Jakou metriku pocitame? (objem, povrch) ")

if metrika == "objem":
    print("Vypocitam objem.")
elif metrika == "povrch":
    print("Vypocitam povrch.")
else:
    print("Neznamy typ metriky.")
    quit()

velikost = int(input("Delka strany (krychle, kvadr) nebo prumeru (koule) v cm? "))
if velikost <= 0:
    print("Cislo musi byt kladne.")
    quit()
if teleso == "krychle":
    if metrika == "objem":
        objem = velikost ** 3
        print("Objem krychle je", objem)
    elif metrika == "povrch":
        povrch = 6 * (velikost ** 2)
        print("Povrch krychle je", povrch)
elif teleso == "koule":
    if metrika == "objem":
        objem = (4/3) * 3.14 * ((velikost / 2) ** 3)
        print("Objem koule je", objem)
    elif metrika == "povrch":
        povrch = 4 * 3.14 * ((velikost / 2) ** 2)
        print("Povrch koule je", povrch)
elif teleso == "kvadr":
    vyska = int(input("Zadej vysku kvadru (napis cislo): "))
    if vyska <= 0:
        print("Cislo musi byt kladne.")
        quit()
    if metrika == "objem":
        objem = velikost * velikost * vyska
        print("Objem kvadru je", objem)
    elif metrika == "povrch":
        povrch = 2 * (velikost * velikost + velikost * vyska + velikost * vyska)
        print("Povrch kvadru je", povrch)
