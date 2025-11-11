from turtle import forward, left, right, exitonclick
from math import sqrt

# délka strany domečku
strana = 50

# nakresli domeček jedním tahem s překřížením uvnitř, použij odmocninu ze 2
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

exitonclick()