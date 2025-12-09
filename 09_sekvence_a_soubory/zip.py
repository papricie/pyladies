veci = ['tráva', 'slunce', 'mrkev', 'list']
barvy = ['zelená', 'žluté', 'oranžová', 'zelený']

zip(veci, barvy) # vytvoří zip objekt, dvojice prvků z obou sekvencí
#<zip object at 0x7f0db61b1f48>

list(zip(veci, barvy)) # převede zip objekt na seznam dvojic
#[('tráva', 'zelená'), ('slunce', 'žluté'), ('mrkev', 'oranžová'), ('list', 'zelený')]

for vec, barva in zip(veci, barvy): # projde všechny dvojice prvků z obou sekvencí
    print(f"{vec} je {barva}") # vypíše každý prvek s jeho odpovídající barvou
#tráva je zelená
#slunce je žluté
#mrkev je oranžová
#list je zelený





veci = ['tráva', 'slunce', 'mrkev', 'list'] # první sekvence
barvy = ['zelená', 'žluté', 'oranžová', 'zelený'] # druhá sekvence
mista = ['na zemi', 'nahoře', 'na talíři', 'na stromě'] # třetí sekvence
cisla = range(4) # sekvence čísel od 0 do 3

for vec, barva, misto, cislo in zip(veci, barvy, mista, cisla): # projde všechny čtveřice prvků z obou sekvencí
    print(f"{cislo}. {barva} {vec} je {misto}") # vypíše každý prvek s jeho odpovídající barvou a místem
# 0. zelená tráva je na zemi
# 1. žluté slunce je nahoře
# 2. oranžová mrkev je na talíři
# 3. zelený list je na stromě