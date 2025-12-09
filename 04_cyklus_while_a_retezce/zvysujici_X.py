#Napiš program, který postupně z jednotlivých 'X' vypíše:

#X
#X X
#X X X
#X X X X
#Počet řádků zadá uživatel.

#„Z jednotlivých 'X'“ opět znamená, že každý print vypíše maximálně jedno 'X'.

pocet_radku = int(input("Zadej počet řádků: ")) 
radek = 0
while radek < pocet_radku: # vnější cyklus pro řádky
    sloupec = 0 # vnitřní cyklus pro sloupce
    while sloupec <= radek: # podmínka vnitřního cyklu
        print("X", end=" ") 
        sloupec += 1
    print()
    radek += 1