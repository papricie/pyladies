# Napiš funkci, která dostane seznam souřadnic 
# (párů čísel menších než 10, která určují sloupec a řádek), 
# a vypíše je jako mapu: mřížku 10×10, kde na políčka, 
# která jsou v seznamu napíše X, jinde tečku.

# Vzpomeň si, jak se vypisuje tabulka: 
# pomocí dvou cyklů for zanořených do sebe.
# Pro každou buňku tabulky (tedy vevnitř v cyklu) 
# si vytvoř dvojici radek_a_sloupec = (cislo_radku, cislo_sloupce).
# Napiš X, pokud je dvojice radek_a_sloupec v seznamu. Jinak napiš ..
# Slova jako „souřadice“ a „pozice“ bohužel vypadají v jednotném 
# i množném čísle stejně. Aby ses nezamotala, doporučuju proměnnou 
# s jednou dvojicí pojmenovat radek_a_sloupec a seznam několika 
# takových dvojic seznam_souradnic.


def nakresli_mapu(seznam_souradnic, jidlo): # přidán parametr jidlo
    """
    Vytvoří mapu 10x10 jako řetězec, kde na poziích
    uvedených v seznamu_souradnic jsou:
    'X' je had 
    '.' je prázdné pole
    '?' je jídlo
    """
    mapa = ""
    for radek in range(20): # vnější cyklus pro řádky
        for sloupec in range(20): # vnitřní cyklus pro sloupce
            radek_a_sloupec = (sloupec, radek) # vytvoření dvojice (sloupec, radek)
            if radek_a_sloupec in seznam_souradnic: # kontrola, zda je dvojice v seznamu souřadnic
                mapa += "X " # přidání 'X' na danou pozici
            elif radek_a_sloupec in jidlo: # kontrola, zda je dvojice v seznamu jídla
                mapa += "? " # přidání '?' na danou pozici
            else:
                mapa += ". " # přidání '.' na danou pozici

        mapa += "\n" # přechod na nový řádek po dokončení jednoho řádku

    return mapa


# print(nakresli_mapu([(0, 0), (0, 1), (2, 2), (3, 4), (9, 8)]))
# prvni cislo je sloupec, druhe rade, prvni X je tedy (0, 0)
# posledni X v mape je (9, 9) na konci 10. radku a 10. sloupce
