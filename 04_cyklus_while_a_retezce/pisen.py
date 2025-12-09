# Najdi na internetu text své oblíbené písně, 
# zkopíruj si ho do řetězce a zjisti, 
# kolikrát je v něm použito písmeno K. (Velké nebo malé.) 
# Vyhni se použití count().

# Text by mělo jít jednoduše vyměnit za jiný.

text_pisne = """Mezi námi je mnoho chvil
A pokusů, abych se ti zavděčil
Jenomže od tebe se člověk moc nedoví
Stále básníš o ňákém svém záhadném Čendovi

Je toho moc a to já nesnesu
Zašel jsem na Čendovu adresu
A Čenda před domem zpíval rock n roll
Pro dívky, které se tam denně schází cestou 
z různých škol

Podívej mám styl Čendy
Nevím, kde ho Čenda vzal
A já ho sebral od něho
A on si ho moc nehlídal"""

pocet_k = 0
for znak in text_pisne:
    if znak == "k" or znak == "K":
        pocet_k += 1
print("Počet písmen K nebo k v písni je:", pocet_k)
