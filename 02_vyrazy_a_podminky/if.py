
# Příkaz if slouží k podmíněnému provedení části kódu.
# Pokud je splněna zadaná podmínka, provede se blok kódu za if.
# Pokud není podmínka splněna, blok kódu se přeskočí.
strana = float(input('Zadej stranu čtverce v centimetrech: '))
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
else:
    print('Strana musí být kladná, jinak z toho nebude čtverec!')

print('Děkujeme za použití geometrické kalkulačky.')


# Jednoduchý příkaz if bez větve else:
cislo = int(input('Zadej číslo, přičtu k němu 3: '))
if cislo == 0:
    print('Jé, to je jednoduché!')
print(cislo, '+ 3 =', cislo + 3)

# Příkaz if může mít i více větví – pomocí elif (zkratka pro "else if"). Následující program nabízí nápoje podle věku zákazníka:
vek = int(input('Kolik ti je let? '))
if vek >= 150:
    print('A ze kterépak jsi planety?')
elif vek >= 18:
    # Tahle větev se např. pro "200" už neprovede.
    print('Můžeme nabídnout: víno, cider, nebo vodku.')
elif vek >= 1:
    print('Můžeme nabídnout: mléko, čaj, nebo vodu')
elif vek >= 0:
    print('Sunar už bohužel došel.')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné
    print('Pro návštěvy z budoucnosti bohužel nemáme nic v nabídce.')

# Vnořené příkazy if – tedy if uvnitř jiného if – se hodí, když je potřeba rozhodnout na základě více podmínek:
stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá?')

if stastna == 'ano':
    # Tenhle kus kódu se provede, když je "šťastná"
    if bohata == 'ano':
        print('Gratuluji!')
    else:
        print('Zkus míň utrácet.')
else:
    # Tenhle kus kódu se provede, když není "šťastná"
    if bohata == 'ano':
        print('Zkus se víc usmívat!')
    else:
        print('To je mi líto.')