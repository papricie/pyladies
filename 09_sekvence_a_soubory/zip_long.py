veci = ['tráva', 'slunce', 'mrkev', 'list', 'myšlenka', 'spravedlnost']
barvy = ['zelená', 'žluté', 'oranžová', 'zelený']
for vec, barva in zip(veci, barvy):
    print(f"{vec} je {barva}")

# Výstup:
# tráva je zelená
# slunce je žluté
# mrkev je oranžová
# list je zelený

# Poznámka: Poslední dvě položky v 'veci' 
# (myšlenka, spravedlnost) nemají odpovídající barvy, takže nejsou vypsány.

from itertools import zip_longest 
for vec, barva in zip_longest(veci, barvy, fillvalue='(nevím)'): # použití fillvalue, pokud chybí hodnota, jinak None
    print(f"{vec} je {barva}")
# Výstup:
# tráva je zelená
# slunce je žluté
# mrkev je oranžová
# list je zelený
# myšlenka je (nevím)
# spravedlnost je (nevím)


for vec, barva in zip_longest(veci, barvy): # výchozí fillvalue je None
    if vec == None: 
        vec = 'nějaká věc' # náhrada za None
    if barva == None:
        barva = 'bez barvy' # náhrada za None
    print(f"{vec} je {barva}") 
# Výstup:
# tráva je zelená
# slunce je žluté
# mrkev je oranžová
# list je zelený
# myšlenka je bez barvy
# spravedlnost je bez barvy