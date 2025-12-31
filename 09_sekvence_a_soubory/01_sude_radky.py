# Napiš program, který vypíše básničku ze souboru basnicka.txt, 
# ale vynechá včechny sudé řádky.

# Zpracovávej ji po jednotlivých řádcích. 
# (Nebudeš tak načítat celou dlouhou báseň jako 
# řetězec do paměti počítače; tvůj program bude 
# vždycky potřebovat místo jen na jeden řádek.)


with open('basnicka.txt', encoding='utf-8') as soubor:
    for cislo_radku, radek in enumerate(soubor):
        if cislo_radku % 2 == 0:  # pokud je číslo řádku sudé
            radek = radek.rstrip()  # odstraní koncové mezery a znaky nového řádku \n
            print(radek)


