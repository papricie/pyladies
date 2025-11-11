celkem = 0

for delka_trasy in 8, 45, 9, 21:
    print('Jdu', delka_trasy, 'km do další vesnice.')
    celkem = celkem + delka_trasy

print('Celkem jsem ušla', celkem, 'km')
#Jdu 8 km do další vesnice.
#Jdu 45 km do další vesnice.
#Jdu 9 km do další vesnice.
#Jdu 21 km do další vesnice.
#Celkem jsem ušla 83 km

# V každém kroku cyklu se k proměnné celkem přičte 
# hodnota delka_trasy.
# Po skončení cyklu tedy proměnná celkem 
# obsahuje součet všech hodnot

# Můžeš si to představit takto:
celkem = 0
celkem = celkem + 8    # první krok cyklu
celkem = celkem + 45   # druhý krok cyklu  
celkem = celkem + 9    # třetí krok cyklu
celkem = celkem + 21   # čtvrtý krok cyklu
# Po skončení cyklu tedy proměnná celkem
# obsahuje součet všech hodnot
print('Celkem jsem ušla', celkem, 'km')
#Celkem jsem ušla 83 km
# Výstup je stejný jako předtím.
# Ale teď už víš, jak to funguje uvnitř!
# V každém kroku cyklu se k proměnné celkem přičte 
# hodnota delka_trasy. 

# Takto by šlo napsat i bez cyklu, ale bylo by to o hodně delší:
celkem = 0

delka_trasy = 8
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

delka_trasy = 45
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

delka_trasy = 9
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

delka_trasy = 21
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

print('Celkem jsem ušla', celkem, 'km')