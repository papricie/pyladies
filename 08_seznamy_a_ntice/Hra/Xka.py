# Úkol na procvičení a vzpomenutí. Už jsi ho jednou vyřešila.

# Pomocí cyklů for a parametru end pro print napiš program, 
# který postupně z jednotlivých 'X' vypíše:

# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# „Z jednotlivých 'X'“ znamená, že každý print vypíše jen jedno X. 
# Nepoužívej tedy např. print('X X X X X') ani print('X ' * 5). 
# Velikost tabulky bude zadaná v programu, program se na ni nebude ptát uživatele.


for radek in range(5): # vnější cyklus pro řádky
    for sloupec in range(5): # vnitřní cyklus pro sloupce
        print("X", end=" ") # print nebude po každém 'X' přecházet na nový řádek, ale místo toho vypíše mezeru
    print()