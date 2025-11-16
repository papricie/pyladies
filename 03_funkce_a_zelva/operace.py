prvni = float(input("První číslo: "))
druhe = float(input("Druhé číslo: "))
operace = input("Operace (+, -, *, /): ")

if operace == "+":
    vysledek = prvni + druhe
elif operace == "-":
    vysledek = prvni - druhe
elif operace == "*":
    vysledek = prvni * druhe
elif operace == "/":
    vysledek = prvni / druhe
else:
    print("Neplatná operace.")
    quit()

print(prvni, operace, druhe, "=", vysledek)
