
# Vytvoř hru Kámen nůžky papír, která funguje následovně:

# Do proměnné tah_pocitace dá náhodně slovo 'kámen', 'nůžky' nebo 'papír'.
# Zeptá se uživatele na tah; výsledek uloží do proměnné tah_hrace

# Je-li tah hráče 'kámen':
# je-li tah počítače 'kámen':
# vypíše 'Remíza!';
# jinak, je-li tah počítače 'nůžky':
# vypíše 'Vyhrál jsi!';
# jinak, je-li tah počítače 'papír':
# vypíše 'Prohrál jsi!'.
# Jinak, je-li tah hráče 'nůžky':
# je-li tah počítače 'kámen':
# vypíše 'Prohrál jsi!';
# jinak, je-li tah počítače 'nůžky':
# vypíše 'Remíza!';
# jinak, je-li tah počítače 'papír':
# vypíše 'Vyhrál jsi!'.
# Jinak, je-li tah hráče 'papír':
# je-li tah počítače 'kámen':
# vypíše 'Vyhrál jsi!';
# jinak, je-li tah počítače 'nůžky':
# vypíše 'Prohrál jsi!';
# jinak, je-li tah počítače 'papír':
# vypíše 'Remíza!'.
# Jinak,
# Omluví se (vypíše hlášku), že zná jen tři slova: kámen, nůžky a papír.

#Je to celkem dlouhý program, ale můžeš ho psát postupně: 
# každý jednotlivý řádek „přelož“ do Pythonu. 
# Budeš potřebovat if, elif, a else; porovnávání (==) a přiřazení (=); pro výpis print a pro vstup input.


from random import randrange
nahodne_cislo = randrange(3)

# tah pocitace
if nahodne_cislo == 0:
    tah_pocitace = "kamen"
elif nahodne_cislo == 1:
    tah_pocitace = "nuzky"
else:
    tah_pocitace = "papir"

# tah hrace
tah_hrace = input("Zadej svuj tah (kamen, nuzky, papir): ")
# vyhodnoceni
# kamen
if tah_hrace == "kamen":
    if tah_pocitace == "kamen":
        print("Remiza")
    elif tah_pocitace == "nuzky":
        print("Vyhra")
    elif tah_pocitace == "papir":
        print("Prohra")
# nuzky            
elif tah_hrace == "nuzky":
    if tah_pocitace == "kamen":
        print("Prohra")
    elif tah_pocitace == "nuzky":
        print("Remiza")
    elif tah_pocitace == "papir":
        print("Vyhra")
# papir
elif tah_hrace == "papir":
    if tah_pocitace == "kamen":
        print("Vyhra")
    elif tah_pocitace == "nuzky":
        print("Prohra")
    elif tah_pocitace == "papir":
        print("Remiza")
# spatny vstup
else:
    print("Omlouvam se, ale znam jen tri slova: kamen, nuzky a papir")