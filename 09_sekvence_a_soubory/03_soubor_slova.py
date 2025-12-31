# Slova ze seznamu vytvořeného výše ulož do souboru slova.txt, 
# kde bude na každém řádku jedno slovo.

from slovnik import slova
with open('slova.txt', 'w', encoding='utf-8') as vystupni_soubor:
    for slovo in slova:
        vystupni_soubor.write(slovo + '\n')
