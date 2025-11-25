# Pomocí cyklu for napiš program, který vypíše:

# 0 na druhou je 0
# 1 na druhou je 1
# 2 na druhou je 4
# 3 na druhou je 9
# 4 na druhou je 16
# Jak pojmenuješ proměnnou cyklu?

for cislo in range(5):
    print(str(cislo) + " na druhou je " + str(cislo ** 2))