# Napiš funkci mocniny, která pro argumentem zadané 
# číslo n vytvoří a vrátí slovník, kde jako klíče 
# budou čísla od jedné do n a jako hodnoty 
# k nim jejich druhé mocniny.

# Například: mocniny(4) 
# vrátí {1: 1, 2: 4, 3: 9, 4: 16}

def mocniny(n): #
    vysledek = {} 
    for i in range(1, n + 1): # iterace od 1 do n
        vysledek[i] = i ** 2 # přidání klíče a hodnoty do slovníku
    return vysledek

# print(mocniny(4))  # {1: 1, 2: 4, 3: 9, 4: 16}


