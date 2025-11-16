from turtle import forward, left, right, exitonclick
from math import sqrt

strana = 50

# tři svislé + vodorovné stěny lze kreslit cyklem
left(90)
for _ in range(3):
    forward(strana)
    right(90)
    forward(strana)
    left(90)

# šikmá úsečka
right(135)
forward(sqrt(2) * strana)

# dokončení překřížení uvnitř
left(135)
forward(strana)
left(45)
forward(strana / sqrt(2))
left(90)
forward(strana / sqrt(2))
left(90)
forward(sqrt(2) * strana)

exitonclick()
