slovo = 'Ahoj'
delka = len(slovo)      # Vypočítání délky
print(delka)
# 4

###

vysledek = 3 * (5 + 2)
#              ╰──┬──╯
vysledek = 3 *    7
#          ╰─┬────╯
vysledek =  21
print(vysledek)
# 21

###

vysledek = len("Ahoj!")
#          ╰────┬─────╯
vysledek =      5
print(vysledek)
# 5

###

delka = len('Ahoj') + len('!')
#        ╰──┬─────╯    ╰─┬───╯
delka =     4       +    1
#           ╰───────┬────╯
delka =             5
print(delka)
# 5

###

if len('Ahoj!') <= 3:
    print('pozdrav je krátký')
#  len('Ahoj!') <= 3
#  ╰─────┬────╯
#        5      <= 3
#        ╰──────┬──╯
#             False
# (žádný výstup)
if len('Cau') <= 3:
    print('pozdrav je krátký')
# pozdrav je krátký


###


x = 5
print(len('Ahoj') + x)
#     ╰────┬────╯   |
print(     4      + 5)
#          ╰───┬────╯
print(         9     )
# 9

###

print(1, 2, 3, 4)         # Výchozí oddělovač je mezera
# 1 2 3 4
print(1, 2, 3, 4, sep=', ')     # Místo mezery odděluj čárkou a mezerou
# 1, 2, 3, 4


###


print('1 + 2', end=' ')     # Místo přechodu na nový řádek jen napiš mezeru
print('=', end=' ')
print(1 + 2, end='!')
print()
# 1 + 2 = 3!

###

print(len('a'))     # Volání funkce (a vypsání výsledku)
# 1
print(len)          # Vypsání samotné funkce
# <built-in function len>
print(len + 1)      # Sečtení funkce a čísla
# TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'int'



