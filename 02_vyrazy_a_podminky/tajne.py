# Program, kde uživatel hadá tajné číslo

# uživatel hádá čísla od 1 do 10
tajne_cislo = 7
zadane_cislo = float(input("Uhodni číslo od 1 do 10 a dozvíš se tajemství: "))
# kontrola, zda je číslo v povoleném rozsahu
if zadane_cislo < 1 or zadane_cislo > 10:
    print("Číslo musí být opravdu v rozmezí od 1 do 10.")
elif zadane_cislo == tajne_cislo:
    print("Správně, tajemství je, že mi nejde vymyslet tajemství.")
else:
    print("Škoda, nic se nedozvíš.")