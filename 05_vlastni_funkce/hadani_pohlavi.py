# Napiš funkci, která jako argument bere příjmení uživatelky/uživatele 
# a zkusí podle něj uhodnout její/jeho pohlaví. To vrátí jako řetězec.

# Funkci v programu několikrát zavolej (s různými příjmeními – 
# ty můžeš zadat přímo do kódu při volání funkcí). Výsledky vypiš.

# (Pohlaví není možné určit přesně – stačí zvládnout 
# ta nejčastější česká příjmení.)


def uhodni_pohlavi(prijmeni):
    if prijmeni.endswith("ová"):
        return "žena"
    else:
        return "muž" 

print(uhodni_pohlavi("Svobodová"))
print(uhodni_pohlavi("Svoboda"))
print(uhodni_pohlavi("Nováková"))
print(uhodni_pohlavi("Novák"))




