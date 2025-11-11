from turtle import forward, left, penup, pendown, exitonclick, speed
speed(0)

# seznam počtů stran polygonů
strany_list = [5, 6, 7, 8]

for n in strany_list:
    delka_strany = 200 / n  # délka strany podle n, aby tvary byly zhruba stejně velké
    vnitřní_úhel = 180 * (1 - 2 / n)
    vnější_úhel = 180 - vnitřní_úhel

    # nakreslení n-úhelníku
    pendown()
    for _ in range(n):
        forward(delka_strany)
        left(vnější_úhel)
    penup()

    # posun doprava
    forward(80)  # mezera mezi tvary

exitonclick()