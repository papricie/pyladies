# Napiš cyklus, který se bude ptát uživatele na směr pohybu hada (w, s, d, a),
# podle ní zavolá pohyb, a následně vykreslí seznam jako mapu. 
# Pak se opět se zeptá na stranu atd.

# Začínej se seznamem [(0, 0), (0, 1), (0, 2)].

from mapa import nakresli_mapu
from pohyb_4 import pohyb

seznam_souradnic = [(0, 0), (0, 1), (0, 2)]  
jidlo = [(2, 3), (4, 5)]  # počáteční seznam jídla

# počáteční seznam souřadnic (had leze smerem na jih)
# X . . . . . . . . . 
# X . . . . . . . . . 
# X . . . . . . . . . 
# . . . . . . . . . . 
# . . . . . . . . . . 
# . . . . . . . . . . 
# . . . . . . . . . .
# . . . . . . . . . . 
# . . . . . . . . . . 
# . . . . . . . . . .  

while True:
    print(nakresli_mapu(seznam_souradnic, jidlo)) # pridano jidlo
    smer = input("Zadej směr pohybu (w, s, d, a) nebo 'konec': ").lower()

    if smer.lower() == 'konec':
        print("Konec hry.")
        break

    try:
        pohyb(seznam_souradnic, smer, jidlo) # pridano jidlo
    except ValueError as error:
        print(error) 
    except RuntimeError as error: # pridan RuntimeError
        print(error)
        print("Konec hry.")
        break



