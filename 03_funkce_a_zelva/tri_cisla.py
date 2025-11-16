součet = 0

for i in range(3):
    číslo = float(input("Zadej číslo: "))
    součet += číslo

if součet > 10:
    print("Součet je větší než 10.")
else:
    print("Součet není větší než 10.")
