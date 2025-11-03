
# Čtverec - obvod a obsah
print('Obvod čtverce se stranou 356 cm je', 4 * 356, 'cm') # O = 4a
print('Obsah čtverce se stranou 356 cm je', 356 * 356, 'cm2') # S = a²

# Menší čtverec
print('Obvod čtverce se stranou 123 cm je', 4 * 123, 'cm')
print('Obsah čtverce se stranou 123 cm je', 123 * 123, 'cm2')

# Použití proměnné aby se strana čtverce dala snadno měnit
strana = 123
print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')

# Vstup od uživatele
promenna = input('Zadej text: ')
promenna = int(input('Zadej číslo: '))
promenna = float(input('Zadej číslo: '))

strana = float(input('Zadej stranu čtverce v centimetrech: '))
print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')

