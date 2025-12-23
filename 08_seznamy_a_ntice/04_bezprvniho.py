# Napiš funkci bez_prvniho, která dostane seznam jmen 
# a vrátí seznam se všemi jeho prvky kromě prvního.

# >>> from moje_reseni import vytvor_seznam_zvirat, bez_prvniho
# >>> zvirata = vytvor_seznam_zvirat()
# >>> zvirata
# ['pes', 'kočka', 'králík', 'had']
# >>> bez_prvniho(zvirata)
# ['kočka', 'králík', 'had']
# Funkce opět nesmí změnit původní seznam:

# >>> zvirata
# ['pes', 'kočka', 'králík', 'had']
# A musí fungovat i pro prázdný seznam:

# >>> bez_prvniho([])
# []

from moje_reseni import vytvor_seznam_zvirat, bez_prvniho
zvirata = vytvor_seznam_zvirat() # ['pes', 'kočka', 'králík', 'had']
print(zvirata) # ['pes', 'kočka', 'králík', 'had']
print(bez_prvniho(zvirata)) # ['kočka', 'králík', 'had']
print(bez_prvniho([])) # []
print(zvirata) # ['pes', 'kočka', 'králík', 'had']


