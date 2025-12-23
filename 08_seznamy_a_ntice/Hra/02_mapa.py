# Napiš funkci, která dostane seznam souřadnic 
# (párů čísel menších než 10, která určují sloupec a řádek), 
# a vypíše je jako mapu: mřížku 10×10, kde na políčka, 
# která jsou v seznamu napíše X, jinde tečku. Například:

# nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

# X . . . . . . . . .
# X . . . . . . . . .
# . . X . . . . . . .
# . . . . . . . . . .
# . . . X . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . X 
# . . . . . . . . . .

# Jak na to?

# Vzpomeň si, jak se vypisuje tabulka: 
# pomocí dvou cyklů for zanořených do sebe.
# Pro každou buňku tabulky (tedy vevnitř v cyklu) 
# si vytvoř dvojici radek_a_sloupec = (cislo_radku, cislo_sloupce).
# Napiš X, pokud je dvojice radek_a_sloupec v seznamu. Jinak napiš ..
# Slova jako „souřadice“ a „pozice“ bohužel vypadají v jednotném 
# i množném čísle stejně. Aby ses nezamotala, doporučuju proměnnou 
# s jednou dvojicí pojmenovat radek_a_sloupec a seznam několika 
# takových dvojic seznam_souradnic.



# def nakresli_mapu(seznam_souradnic):
    # for radek in range(10): # vnější cyklus pro řádky
        # for sloupec in range(10): # vnitřní cyklus pro sloupce
            # radek_a_sloupec = (sloupec, radek)
            # if radek_a_sloupec in seznam_souradnic:
            #     print("X", end=" ")
            # else:
            #     print(".", end=" ")
        # print()

# nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

# napis to funkci s return, ne jako program:
def nakresli_mapu(seznam_souradnic):
    """
    Vytvoří mapu 10x10 jako řetězec, kde na pozicích
    uvedených v seznamu_souradnic jsou 'X' a '.'
    """
    mapa = ""
    for radek in range(10): # vnější cyklus pro řádky
        for sloupec in range(10): # vnitřní cyklus pro sloupce
            radek_a_sloupec = (sloupec, radek) # vytvoření dvojice (sloupec, radek)
            if radek_a_sloupec in seznam_souradnic: # kontrola, zda je dvojice v seznamu
                mapa += "X " # přidání 'X' na danou pozici
            else: 
                mapa += ". " # přidání '.' na danou pozici
        mapa += "\n" # přechod na nový řádek po dokončení řádku
    return mapa 

print(nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)]))
# prvni cislo je radek, druhe sloupec

