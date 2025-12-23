# Napiš funkci filtruj_k, která dostane seznam řetězců 
# a vrátí seznam těch, které začínají na k.

# Například:
# >>> from moje_reseni import vytvor_seznam_zvirat, filtruj_k
# >>> zvirata = vytvor_seznam_zvirat()
# >>> filtruj_k(zvirata)
# ['kočka', 'králík']
# Funkce musí opět vracet nový seznam a svůj argument nechat nezměněný.

from moje_reseni import vytvor_seznam_zvirat, filtruj_k
zvirata = vytvor_seznam_zvirat()  # Vytvoření seznamu zvířat
print(filtruj_k(zvirata))  # Očekávaný výstup: ['kočka', 'králík']
print(zvirata)  # Původní seznam zůstal nezměněn ['pes', 'kočka', 'králík', 'had']

