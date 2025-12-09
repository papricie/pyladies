# Toto:

with open('basnicka.txt', encoding='utf-8') as soubor:
    # Zpracování souboru
    obsah = soubor.read()

# je zkratka pro:

soubor = open('basnicka.txt', encoding='utf-8')
try:
    # Zpracování souboru
    obsah = soubor.read()
finally:
    # Ukončení kontextu
    soubor.close()


# Příkaz with tedy zajistí, že se soubor správně zavře i v případě,
# že během zpracování dojde k chybě (výjimce).
print(obsah)
