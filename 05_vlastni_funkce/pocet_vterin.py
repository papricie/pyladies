# Vytvoř funkci pocet_vterin, která bude mít dva argumenty: 
# čas v minutách a čas ve vteřinách a bude vracet celkový počet vteřin.

def pocet_vterin(minuty, sekundy):
    """Funkce vrátí počet vteřin odpovídajících zadaným minutám a sekundám."""
    return minuty * 60 + sekundy

print(pocet_vterin(3, 25))
print(pocet_vterin(0, 45)) 