def uhodni_pohlavi(prijmeni):
    if prijmeni.endswith("ová"):
        return "žena"
    else:
        return "muž" 

print(uhodni_pohlavi("Svobodová"))
print(uhodni_pohlavi("Svoboda"))
print(uhodni_pohlavi("Nováková"))
print(uhodni_pohlavi("Novák"))




