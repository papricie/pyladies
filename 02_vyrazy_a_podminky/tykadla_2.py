# V2 zobrazi pouze jednu zpravu pri splneni podminky (if+elif)
pocet_tykadel = float(input("Zadej počet tykadel: "))

if pocet_tykadel > 12:
    print("Odkud jste přiletěli?")
elif pocet_tykadel > 6:
    print("Že by pavouček?")
else:
    print("Tak málo tykadel mě nezajímá!")