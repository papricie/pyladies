# Napiš funkci vytvor_balicek, která vrátí nový zamíchaný 
# seznam hracích karet pro hru Prší. Každá položka seznamu 
# bude (na rozdíl od balíčku z lekce) dvojice hodnota-barva.

# Hodnoty karet jsou 2-10, 'J', 'Q', 'K', 'A'. 
# Barvy jsou '♥' '♦' '♠' '♣'. 
# (Symboly si můžeš zkopírovat jako text. 
# Nezobrazují-li se ti v příkazové řádce správně, 
# použij místo nich S, K, P, +.)

# Například:
# >>> from moje_reseni import vytvor_balicek
# >>> vytvor_balicek()
# [(2, '♥'), (10, '♠'), ('A', '♣'), ...


from moje_reseni import vytvor_balicek

balicek = vytvor_balicek()
print(balicek)  # vypíše zamíchaný balíček karet jako seznam dvojic (hodnota, barva)


