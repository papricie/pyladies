# Napiš program, který vypíše básničku 
# ze souboru basnicka.txt VELKÝMI PÍSMENY.

# Zpracovávej ji po jednotlivých řádcích. 
# (Nebudeš tak načítat celou dlouhou báseň jako řetězec 
# do paměti počítače; tvůj program bude vždycky 
# potřebovat místo jen na jeden řádek.)

with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        radek = radek.rstrip()  # odstraní koncové mezery a znaky nového řádku \n
        print(radek.upper())    # vypíše řádek VELKÝMI PÍSMENY pomocí metody upper()
