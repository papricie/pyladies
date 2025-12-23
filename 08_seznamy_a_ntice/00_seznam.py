# Napiš funkci vytvor_seznam_zvirat(), 
# která vytvoří nový seznam domácích zvířat a vrátí ho. 
# Domácí zvířata známe tato: "pes", "kočka", "králík", "had".

# Tuto funkci použiješ pro otestování dalších úloh. Nehledej v ní nic složitého.

# Příklad:

# >>> vytvor_seznam_zvirat()
# ['pes', 'kočka', 'králík', 'had']
# Každé zavolání funkce musí vytvořit nový, nezávislý seznam. 
# Vyzkoušej si to následujícím „dialogem“:

# >>> from moje_reseni import vytvor_seznam_zvirat
# >>> zvirata = vytvor_seznam_zvirat()
# >>> zvirata.pop()
# 'had'
# >>> vytvor_seznam_zvirat()
# ['pes', 'kočka', 'králík', 'had']
# >>> zvirata
# ['pes', 'kočka', 'králík']

from moje_reseni import vytvor_seznam_zvirat
# Vytvoření a vrácení nového seznamu domácích zvířat
print(vytvor_seznam_zvirat())   # ['pes', 'kočka', 'králík', 'had']

print("----- Test -----")
zvirata = vytvor_seznam_zvirat() # Vytvoření nového seznamu zvířat
zvirata.pop() # Odstranění posledního zvířete ('had') ze seznamu zvirata
print(vytvor_seznam_zvirat())   # ['pes', 'kočka', 'králík', 'had']
print(zvirata)                  # ['pes', 'kočka', 'králík']
print(vytvor_seznam_zvirat())   # ['pes', 'kočka', 'králík', 'had']