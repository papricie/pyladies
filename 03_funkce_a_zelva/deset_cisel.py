součet = 0

for i in range(10):
    číslo = float(input("Zadej číslo: "))
    součet += číslo

if součet > 1000:
    print("Součet je větší než 1000.")
else:
    print("Součet není větší než 1000.")
