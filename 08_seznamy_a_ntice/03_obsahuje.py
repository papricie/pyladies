# Napiš funkci obsahuje, která dostane seznam 
# a slovo a zjistí, jestli je to slovo v daném seznamu. 
# Podle toho vrátí True nebo False.

# Například:
#>>> from moje_reseni import vytvor_seznam_zvirat, obsahuje
#>>> zvirata = vytvor_seznam_zvirat()
#>>> obsahuje(zvirata, 'pes')
#True
#>>> obsahuje(zvirata, 'vodováha')
#False

from moje_reseni import vytvor_seznam_zvirat, obsahuje
zvirata = vytvor_seznam_zvirat()  # Vytvoření seznamu zvířat
print(obsahuje(zvirata, 'pes'))        # Očekávaný výstup: True
print(obsahuje(zvirata, 'vodováha'))  # Očekávaný výstup: False 