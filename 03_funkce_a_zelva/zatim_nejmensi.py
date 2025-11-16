zatim_nejmensi = 0

for i in range(5):
    cislo = float(input("Zadej číslo: "))
    if i == 0 or cislo < zatim_nejmensi:
        zatim_nejmensi = cislo

print("Nejmenší číslo je:", zatim_nejmensi)
