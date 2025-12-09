print('Slyšela jsem tuto básničku:')
print()

with open('basnicka.txt', encoding='utf-8') as soubor: 
    for radek in soubor: # prochází řádek po řádku
        print('    ' + radek) # odsazení řádku

print()
print('Jak se ti líbí?')
# Vypsání básničky s odsazením řádků

#basnicka

#basnick

#basnic


# Funkce print pak přidá další nový řádek, 
# protože ta na konci výpisu vždycky odřádkovává 
# – pokud nedostane argument end=''.


# Lepší způsob s odstraněním koncových mezer pomocí rstrip()
print('Slyšela jsem tuto básničku:')
print()

with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        radek = radek.rstrip() # odstraní koncové mezery a znaky nového řádku \n, které jsou ve čteném řádku
        print('    ' + radek)

print()
print('Jak se ti líbí?')
# Vypsání básničky s odstraněním koncových mezer \n

#basnicka
#basnick
#basnic