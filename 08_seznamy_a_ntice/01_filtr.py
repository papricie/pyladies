# Napiš funkci filtruj_kratka_jmena, 
# která dostane seznam řetězců a vrátí seznam těch, 
# které jsou kratší než 5 znaků.

# Například:
# >>> from moje_reseni import vytvor_seznam_zvirat, filtruj_kratka_jmena
# >>> zvirata = vytvor_seznam_zvirat()
# >>> filtruj_kratka_jmena(zvirata)
# ['pes', 'had']
# Vzpomeň si, jak se vytváří seznam: začni s prázdným seznamem 
# a postupně přidávej prvek po prvku.
# Funkce musí opět vracet nový seznam a svůj argument nechat nezměněný. 
# Vyzkoušej si to následujícím „dialogem“:

# >>> from moje_reseni import vytvor_seznam_zvirat, filtruj_kratka_jmena
# >>> zvirata = vytvor_seznam_zvirat()
# >>> filtruj_kratka_jmena(zvirata)
# ['pes', 'had']
# >>> zvirata
# ['pes', 'kočka', 'králík', 'had']

from moje_reseni import vytvor_seznam_zvirat, filtruj_kratka_jmena
zvirata = vytvor_seznam_zvirat()  # Vytvoření seznamu zvířat
print(filtruj_kratka_jmena(zvirata))  # Očekávaný výstup: ['pes', 'had']
print(zvirata)  # Původní seznam zůstal nezměněn ['pes', 'kočka', 'králík', 'had']

