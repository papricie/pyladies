# Najdi na internetu text své oblíbené písně, 
# zkopíruj si ho do řetězce a zjisti, 
# kolik je v něm písmen. Nepočítej mezery, 
# znaky nového řádku a znaky 
# !"#$%&\'()*+,-./:;<=>?@[\]^_{|}~.

#Text písně by mělo jít jednoduše vyměnit za jiný.

#Postup:

#Na začátku nastav počet nalezených písmen na 0.
#Pro každý znak textu:
#Když znak není obsažen v ! " # $ % & … :
#Zvyš počet nalezených písmen o 1.
#Vypiš počet nalezených písmen.

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

pocet_znaku = 0
for znak in text_pisne:
    if not znak in ' !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~\n':
        pocet_znaku += 1
print("Počet písmen v písni je:", pocet_znaku)