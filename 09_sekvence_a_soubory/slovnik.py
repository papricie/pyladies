# Stáhni si soubor slovnik.txt se všemi českými slovy.
# Soubor není úplně „čistý“. Vytvoř seznam, kde budou opravdu jen slova:

# Vytvoř prázdný seznam.
# Projdi  po řádcích souboru slovnik.txt a postupně přidávej slova do seznamu.
# Na začátku souboru (řádek 0) je údaj s počtem řádků, ten do seznamu nepřidávej. 
# (Jak při průchodu souborem – sekvencí – zjistíš číslo prvku?)

# Některá slova obsahují další informace za znakem /. 
# Tyto informace (i s lomítkem) ze slov odstraň. 
# Bude se hodit umět slovo rozdělit podle /, viz tahák na seznamy.

# Můžeš se rozhodnout odstranit i slova začínající velkým písmenem. 
# (Většinou jde o vlastní jména a zkratky).

slova = []
with open('slovnik.txt', encoding='utf-8') as soubor:
    for cislo_radku, radek in enumerate(soubor):
        radek = radek.rstrip()  # odstraní koncové mezery a znaky nového řádku \n
        if cislo_radku == 0:
            continue  # přeskočí první řádek s počtem slov
        slovo = radek.split('/')[0]  # vezme část před lomítkem
        if slovo and not slovo[0].isupper():  # zkontroluje, zda nezačíná velkým písmenem
            slova.append(slovo)  # přidá slovo do seznamu
print(slova)