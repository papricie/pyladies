#Napiš program, který z jednotlivých 'X' vypíše pyramidu. Nezapomeň na správné odsazení.

#Příklad:

#    X
#   X X
#  X X X
# X X X X
#X X X X X
#Počet řádků zadá uživatel.

#„Z jednotlivých 'X'“ opět znamená, že každý print vypíše maximálně jedno 'X'.

pocet_radku = int(input("Zadej počet řádků: "))
for radek in range(pocet_radku):
    for mezera in range(pocet_radku - radek - 1): # mezery na začátku řádku
        print(" ", end="") # X s mezerami
    for x in range(radek + 1):
        print("X", end=" ")
    print()  # nový řádek po každém řádku
