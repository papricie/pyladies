soubor = open('basnicka.txt', encoding='utf-8') # otevření souboru, kodování UTF-8
obsah = soubor.read() # přečtení celého obsahu souboru do proměnné
soubor.close() # nezapomeneme zavřít soubor

print(obsah) # vypsání obsahu souboru


# Lepší způsob - s využitím příkazu with, která se postará o zavření souboru
# with open('basnicka.txt', encoding='utf-8') as soubor: # otevření souboru s automatickým zavřením
    # obsah = soubor.read() # přečtení celého obsahu souboru do proměnné

# print(obsah) # vypsání obsahu souboru