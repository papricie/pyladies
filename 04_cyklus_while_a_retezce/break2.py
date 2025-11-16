for i in range(10):  # Vnější cyklus
    for j in range(10):  # Vnitřní cyklus
        print(j * i, end=' ') # Vytiskne násobek i a j
        if i <= j: # Pokud je i menší nebo rovno j, ukončí vnitřní cyklus
            break
    print() # Nový řádek po dokončení vnitřního cyklu

# vysvětlení:
# V tomto příkladu máme dva vnořené cykly:
# - Vnější cyklus iteruje přes hodnoty i od 0 do 9.
# - Vnitřní cyklus iteruje přes hodnoty j od 0 do 9.
# Když je podmínka i <= j splněna, 
# příkaz break ukončí pouze vnitřní cyklus.
# Poté se pokračuje s dalším průchodem vnějšího cyklu.
# Výstupem bude násobková tabulka,
# kde každý řádek obsahuje násobky čísla i až do i * i.
# Tento příklad ilustruje, jak příkaz break ovlivňuje 
# pouze nejbližší obalující cyklus, což umožňuje 
# kontrolovat tok programu ve víceúrovňových strukturách.