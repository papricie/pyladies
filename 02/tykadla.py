# V1 muze zobrazit vice zprav pri splneni podminek (2x if)
pocet_tykadel = float(input("Zadej počet tykadel: "))

if pocet_tykadel > 12:
    print("Odkud jste přiletěli?")
if pocet_tykadel > 6:
    print("Že by pavouček?")
else:
    print("Tak málo tykadel mě nezajímá!")