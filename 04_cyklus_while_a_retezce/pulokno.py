#Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' vypíše:

# X X X X X X
# X         X
# X         X
# X         X
# X         X
# X X X X X X
#„Z jednotlivých 'X'“ opět znamená, že každý print vypíše maximálně jedno 'X'.

for radek in range(6): # vnější cyklus pro řádky
    for sloupec in range(6): # vnitřní cyklus pro sloupce
        if radek == 0 or radek == 5 or sloupec == 0 or sloupec == 5: # podmínka pro okraje
            print("X", end=" ") # tisk 'X' na okrajích
        else: # vnitřek
            print(" ", end=" ") # tisk mezery uvnitř
    print() # nový řádek po každém řádku