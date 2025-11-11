
# Přerušovaná čára
from turtle import forward, penup, pendown, exitonclick

forward(30)
penup()         # od teď želva nekreslí
forward(5)
pendown()       # od teď želva zase kreslí
forward(30)

exitonclick()