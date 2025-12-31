# Napiš funkci pocet_znaku, která jako argument dostane řetězec 
# a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky 
# ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků 
# v řetězci.

# Například: pocet_znaku("hello world") vrátí 
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def pocet_znaku(retezec):
    vysledek = {}
    for znak in retezec:  # iterace přes každý znak v řetězci
        if znak in vysledek:  # pokud je znak již ve slovníku
            vysledek[znak] += 1  # zvýšení počtu výskytů o 1
        else:
            vysledek[znak] = 1  # přidání znaku do slovníku s počtem 1
    return vysledek

print(pocet_znaku("hello world"))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
 
