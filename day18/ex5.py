from secrets import choice
from turtle import Turtle, Screen
import turtle as t
from random import randint

t.colormode(255)
tom_the_turtle = Turtle()
tom_the_turtle.shape("classic")
tom_the_turtle.speed("fastest")
def color():
    digit1 = randint(0, 255)
    digit2 = randint(0, 255)
    digit3 = randint(0, 255)
    return (digit1, digit2, digit3)

def draw_cirle(angle):
    tom_the_turtle.color(color())
    tom_the_turtle.circle(100)
    tom_the_turtle.setheading(angle)
    
for angle in range(1, 361):
   if angle % 5 == 0:
       draw_cirle(angle)
       





screen = Screen()
screen.exitonclick()