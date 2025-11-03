# Program, který spočítá povrch a objem krychle

# uživatel zadá délku strany krychle v cm
a = float(input("Zadej délku strany krychle (v cm): "))
if a <= 0:
    print("Délka strany musí být kladné číslo.")
    exit()

# povrch S = 6a²
S = 6 * a ** 2
# objem V = a³
V = a ** 3

print("Povrch krychle:", S, "cm²")
print("Objem krychle:", V, "cm³")