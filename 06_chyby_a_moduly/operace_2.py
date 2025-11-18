while True:
    prvni = float(input("První číslo: "))
    try:
        float(prvni)
        break
    except ValueError:
        print("Toto není číslo")

while True:
    druhe = float(input("Druhé číslo: "))
    try:
        float(druhe)
        break
    except ValueError:
        print("Toto není číslo")


operace = input("Operace (+, -, *, /): ")

if operace not in ["+", "-", "*", "/"]:
    raise ValueError("Neplatné znamínko")

if operace == "+":
    vysledek = prvni + druhe
elif operace == "-":
    vysledek = prvni - druhe
elif operace == "*":
    vysledek = prvni * druhe
elif operace == "/":
    if druhe == 0:
        raise ValueError("Nelze dělit nulou")
    vysledek = prvni / druhe
else:
    raise ValueError("Neplatná operace")
print(prvni, operace, druhe, "=", vysledek)
