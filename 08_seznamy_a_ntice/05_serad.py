# Had byl pyšný na to, že je v abecedě první. 
# Dokud nepřiletěla "andulka".

# Abys hada uklidnila, vytvoř funkci serad_od_druheho, 
# která zvířata seřadí podle abecedy, 
# ale bude ignorovat první znak. Například:

# >>> from moje_reseni import vytvor_seznam_zvirat, serad_od_druheho
# >>> zvirata = vytvor_seznam_zvirat()
# >>> serad_od_druheho(zvirata)
# ["had", "pes", "andulka", "kočka", "králík"]
# >>> # (barvy jsou tu jen pro přehlednost, tvůj program vypisuje bez barev)
# Máš tady seznam hodnot, které chceš seřadit podle nějakého klíče. 
# Klíč se dá z každé hodnoty vypočítat 
# – v našem případě je to hodnota kromě prvního znaku 
# (tedy od druhého znaku dál).

# Postup:
#
# Vytvoř seznam dvojic (klíč, hodnota).
# Seřaď tento seznam dvojic – dvojice se řadí nejdřív podle 
# prvního prvku, pak druhého atd.
# Nakonec vytvoř ze seznamu dvojic výsledný seznam hodnot.
# Vytvoření seznamu se dělá tak, že začneš s prázdným seznamem 
# a postupně do něj přidáváš hodnoty jednu po druhé.

from moje_reseni import vytvor_seznam_zvirat, serad_od_druheho
zvirata = vytvor_seznam_zvirat() # ['andulka', 'had', 'kočka', 'králík', 'pes'] 
print(zvirata) # zvirata podle abecedy
print(serad_od_druheho(zvirata)) # zvirata serazena podle druheho znaku (a,e,n,o,r)
# ['had', 'pes', 'andulka', 'kočka', 'králík']
