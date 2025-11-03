# Program, který vypisuje hlášky dle zadaných vstupních hodnot
mnozstvi_kavy = float(input("Zadej počet šálků kávy: "))
if mnozstvi_kavy < 0:
    print("Počet šálků kávy nemůže být záporný.")
    exit()
elif mnozstvi_kavy == 0:
    print("Žádný šálek kávy? To je smutné.")
elif 1 <= mnozstvi_kavy <= 3:
    print("Malý kávový nadšenec!")
elif 4 <= mnozstvi_kavy <= 8:
    print("Kávový milovník!")   
elif mnozstvi_kavy > 8:
    print("Tryskomyš!")

else:
    print("Neplatný vstup.")


