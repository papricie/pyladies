# Na tomhle místě programu už se k řetězci 'modrá' nedostaneš...

oblibena_barva = 'modrá'
print(oblibena_barva)
# Oblíbená barva je teď modrá.

oblibena_barva = 'žlutá'
print(oblibena_barva)
# Teď už má oblíbenou barvu žlutou, protože jsme přepsali hodnotu proměnné.


#Trošku zajímavější (nebo složitější?) je situace, kdy hodnotu proměnné přepíšeš výrazem, 
# který používá tu stejnou proměnnou. Zkus si to:

oblibene_cislo = 7
print(oblibene_cislo)
# Oblíbené číslo je teď 7.

oblibene_cislo = oblibene_cislo * 6
print(oblibene_cislo)
# Teď už je oblíbené číslo 42, protože jsme původní hodnotu 7 vynásobili 6.

# Co se tady děje? Python vyhodnotí výraz za = se starou hodnotou proměnné, 
# a teprve když zná výsledek, přiřadí ho (a na starou hodnotu zapomene). 
# V našem příkladu postupuje takhle:

oblibene_cislo = oblibene_cislo * 6
#                ╰──────────┬─╯
oblibene_cislo =            7   * 6
#                           ╰─┬───╯
oblibene_cislo =             42
#         ▲                  |
#         ╰──────────────────╯
print(oblibene_cislo)
# A teď už je oblíbené číslo 42.