dny = ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne']

for index, den in enumerate(dny): # Projde všechny dny s jejich indexy
    cislo = index + 1 # Číslo dne je index + 1
    print(f'{cislo}. {den}') # Vypíše číslo a zkratku dne
#1. Po
#2. Út
#3. St ....

# Stejný kód, ale elegantnejsi s argumentem (parametrem) start=1 u funkce enumerate
for index, den in enumerate(dny, start=1): # Projde všechny dny s jejich indexy, začíná od 1
    print(f'{index}. {den}') # Vypíše číslo a zkratku dne