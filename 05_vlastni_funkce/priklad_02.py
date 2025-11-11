j = 5
while True:
    j = j + 6
    #print(j) necháme si pro ilustraci

# nekonečný cyklus, který vypisuje 
# čísla 11, 17, 23, 29, ...
# ukončíme ho tlačítkem Stop v Thonny 
# nebo klávesovou zkratkou Ctrl+C v terminálu
# pozor, že hodnota j se stále zvětšuje
# může dojít k přetečení paměti nebo zpomalení počítače
# proto je dobré mít v nekonečném cyklu nějakou 
# podmínku pro ukončení
# například:
j = 5
while True:
    j = j + 6
    print(j)
    if j > 50: # podmínka pro ukončení cyklu
        break  # příkaz break ukončí nejbližší obalující cyklus 

