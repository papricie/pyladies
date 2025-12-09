# Napiš program, který se zeptá na dva řetězce a zjistí, 
# jestli je jeden obsažen ve druhém. 
# Nebere přitom ohled na velikost písmen.

retezec1 = str(input("Zadej první řetězec: "))
retezec2 = str(input("Zadej druhý řetězec: "))

if retezec1.lower() in retezec2.lower():
    print(f"Ano, {retezec1} je obsažen v {retezec2}.")
else:
    print(f"Ne, {retezec1} není obsažen v {retezec2}.")
