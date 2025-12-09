#Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' vypíše:
#pocet radku a sloupcu zada uzivatel
# X X X X X X
# X         X
# X         X
# X         X
# X         X
# X X X X X X
#„Z jednotlivých 'X'“ opět znamená, že každý print vypíše maximálně jedno 'X'.

pocet_radku = int(input("Zadej počet řádků: "))
pocet_sloupcu = int(input("Zadej počet sloupců: "))

for radek in range(pocet_radku): # vnější cyklus pro řádky
    for sloupec in range(pocet_sloupcu): # vnitřní cyklus pro sloupce
        if radek == 0 or radek == pocet_radku - 1 or sloupec == 0 or sloupec == pocet_sloupcu - 1: # podmínka pro okraje
            print("X", end=" ") # tisk 'X' na okrajích
        else: # vnitřek
            print(" ", end=" ") # tisk mezery uvnitř
    print() # nový řádek po každém řádku