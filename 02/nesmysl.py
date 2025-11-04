# Program, který podle počtu vypitých šálků kávy za den vypíše odpovídající komentář.
mnozstvi_kavy = int(input("Zadej počet šálků kávy: "))

if mnozstvi_kavy == 0:
    print("Žádný šálek kávy? To je smutné.")
elif mnozstvi_kavy >= 5:
    print("Tryskomyš!")
elif mnozstvi_kavy >= 3:
    print("Kávový milovník!")
elif mnozstvi_kavy >= 1:
    print("Bezva, káva je super!")
else:
    print("Počet šálků kávy nemůže být záporný.")


