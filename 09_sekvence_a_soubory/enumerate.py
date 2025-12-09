trpaslici = ['Prófa', 'Stydlín', 'Dřímal', 'Kejchal', 'Štístko',
             'Šmudla', 'Rejpal']

enumerate(trpaslici)
print(enumerate(trpaslici)) # Vypíše objekt enumerate
# <enumerate object at 0x000001E2C3B4BFC0>

list(enumerate(trpaslici))
print(list(enumerate(trpaslici))) # Vypíše seznam dvojic (index, prvek)
#[(0, 'Prófa'), (1, 'Stydlín'), (2, 'Dřímal'), (3, 'Kejchal'), (4, 'Štístko'), (5, 'Šmudla'), (6, 'Rejpal')]


for dvojice in enumerate(trpaslici): # Projde všechny dvojice
    # Rozbalení dvojice
    index, trpaslik = dvojice
    # Vypsání
    print(f'Na pozici {index} je {trpaslik}!') # Vypíše jednotlivé prvky s jejich indexy
#Na pozici 0 je Prófa!
#Na pozici 1 je Stydlín!
#Na pozici 2 je Dřímal! .....

# rozepsany for cyklus
dvojice = 0, 'Prófa'    # nastavení proměnné dělá `for`
index, trpaslik = dvojice
print(f'Na pozici {index} je {trpaslik}!')

dvojice = 1, 'Stydlín'  # nastavení proměnné dělá `for`
index, trpaslik = dvojice
print(f'Na pozici {index} je {trpaslik}!')

dvojice = 2, 'Dřímal'   # nastavení proměnné dělá `for`
index, trpaslik = dvojice
print(f'Na pozici {index} je {trpaslik}!')

# A tak dále

# rucne bez pomocne promenne dvojice
index, trpaslik = 0, 'Prófa'    # nastavení proměnných
print(f'Na pozici {index} je {trpaslik}!')

index, trpaslik = 1, 'Stydlín'  # nastavení proměnných
print(f'Na pozici {index} je {trpaslik}!')

index, trpaslik = 2, 'Dřímal'   # nastavení proměnných
print(f'Na pozici {index} je {trpaslik}!')

# A tak dále


# for cyklus muze rovnou priradit hodnoty do vice promennych
for index, trpaslik in enumerate(trpaslici):
    print(f'Na pozici {index} je {trpaslik}!')