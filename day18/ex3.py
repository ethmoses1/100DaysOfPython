from turtle import Turtle, Screen
import turtle as t
from random import randint

t.colormode(255)
tom_the_turtle = Turtle()
tom_the_turtle.shape("classic")

def color():
    digit1 = randint(0, 255)
    digit2 = randint(0, 255)
    digit3 = randint(0, 255)
    return (digit1, digit2, digit3)


def draw(side, shape):
    tom_the_turtle.pencolor(color())
    for _ in range(side):
        tom_the_turtle.forward(100)
        tom_the_turtle.right(shape)

for side in range(3, 11):
    angle = 360/side
    draw(side, angle)


screen = Screen()
screen.exitonclick()