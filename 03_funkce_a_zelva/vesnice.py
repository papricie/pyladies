from turtle import forward, left, right, exitonclick, speed
from math import sqrt

speed(0)  # turboželva

# délka strany domečku
strana = 50

# nakresli vesnici s nekolikými domečky jedním tahem s překřížením uvnitř, 
# použij odmocninu ze 2
for i in range(3):  # nakresli 3 domečky
    left(90)
    forward(strana)
    right(90)
    forward(strana)
    right(135)
    forward(sqrt(2) * strana)
    left(135)
    forward(strana)
    left(90)
    forward(strana)
    left(45)
    forward(strana / sqrt(2))
    left(90)
    forward(strana / sqrt(2))
    left(90)
    forward(sqrt(2) * strana)
    left(45)
    forward(strana) # posun na další domeček

exitonclick()