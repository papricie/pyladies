# Napiš program, který se zeptá na dva řetězce a zjistí, 
# jestli je jeden obsažen ve druhém. 
# Nebere přitom ohled na velikost písmen.

retezec1 = "Vek"
retezec2 = "Pravek"

if retezec1.lower() in retezec2.lower():
    print("Ano, Vek je obsažen v Pravek.")
