
# Testování malé násobilky
# Nech počítač náhodně vygenerovat dvě čísla v rozsahu 1 až 10 včetně,
# a uživatele vyzvi k zadání jejich součinu. Ověř, 
# jestli uživatel odpověděl správně.
from random import randrange
cislo1 = randrange(1, 11)
cislo2 = randrange(1, 11)
spravna_odpoved = cislo1 * cislo2
print(cislo1, '*', cislo2, '= ?')
zadana_odpoved = int(input('Zadej svůj výsledek: '))
if zadana_odpoved == spravna_odpoved:
    print('Správně!')
else:
    print('Špatně! Správná odpověď je', spravna_odpoved)