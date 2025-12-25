# Napiš cyklus, který se bude ptát uživatele na světovou stranu, 
# podle ní zavolá pohyb, a následně vykreslí seznam jako mapu. 
# Pak se opět se zeptá na stranu atd.

# Začínej se seznamem [(0, 0), (0, 1), (0, 2)].



from mapa import nakresli_mapu
from pohyb import pohyb

seznam_souradnic = [(0, 0), (0, 1), (0, 2)]  

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
    print(nakresli_mapu(seznam_souradnic))  # vykreslení mapy
    smer = input("Zadej směr pohybu (s, j, v, z) nebo 'konec' pro ukončení: ")  # dotaz na směr
    if smer.lower() == 'konec':  # podmínka pro ukončení cyklu
        print("Konec hry.")
        break
    try:
        pohyb(seznam_souradnic, smer)  # volání funkce pohyb
    except ValueError as error:
        print(error)  # výpis chyby při neplatném vstupu

