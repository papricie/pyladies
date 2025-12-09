zajimava_cisla = range(8, 10000, 3)  # Každé třetí číslo od 8 do 9999
print(zajimava_cisla)  # Vypíše objekt range
#range(8, 10000, 3)
zajimava_cisla[80]          # Osmdesáté "zajímavé číslo"
print(zajimava_cisla[80]) # Vypíše osmdesáté "zajímavé číslo"
#248
zajimava_cisla[:5]          # Prvních 5 "zajímavých čísel"
print(zajimava_cisla[:5]) # Vypíše prvních 5 (3) "zajímavých čísel" ale jako objekt range
#range(8, 23, 3)
list(zajimava_cisla[:5])    # Vypsání prvních 5 "zajímavých čísel"
print(list(zajimava_cisla[:5])) # Vypíše prvních 5 "zajímavých čísel" jako seznam
#[8, 11, 14, 17, 20]
len(zajimava_cisla)         # Kolik tam je čísel?
print(len(zajimava_cisla)) # Vypíše počet "zajímavých čísel"
#3331
1337 in zajimava_cisla      # Je v této sekvenci moje konkrétní číslo ?
print(1337 in zajimava_cisla) # Vypíše, zda je číslo 1337 v sekvenci
#True
zajimava_cisla.index(1337)  # Kolikáté je?
print(zajimava_cisla.index(1337)) # Vypíše pozici čísla 1337 v sekvenci
#443




import random
random.choice(zajimava_cisla)
#????
print(random.choice(zajimava_cisla)) # Vypíše náhodné "zajímavé číslo"




for i in zajimava_cisla: # Projde celou sekvenci
    print(i) # Vypíše jednotlivé prvky sekvence pod sebe
    if i > 20: 
        break  # POZOR až tady vyhodnotí podmínku i > 20 a přeruší cyklus
#8
#11
#14
#17
#20
#23