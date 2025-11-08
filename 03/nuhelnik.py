from turtle import forward, left, exitonclick, speed

speed(0)

# vstup od uživatele
n = int(input("Zadej počet stran n-úhelníku: "))

# délka strany podle n, aby tvary byly zhruba stejně velké
delka_strany = 200 / n

# vnitřní úhel
vnitřní_úhel = 180 * (1 - 2 / n)

# vnější úhel pro turtle (360 / n)
vnější_úhel = 180 - vnitřní_úhel

# nakreslení n-úhelníku
for i in range(n):
    forward(delka_strany)
    left(vnější_úhel)

exitonclick()