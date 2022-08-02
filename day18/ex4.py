from secrets import choice
from turtle import Turtle, Screen
from random import randint

tom_the_turtle = Turtle()
tom_the_turtle.shape("classic")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tom_the_turtle.pensize(15)
tom_the_turtle.speed("fastest")

for _ in range(200):
    tom_the_turtle.color(choice(colours))
    tom_the_turtle.forward(30)
    tom_the_turtle.setheading(choice(directions))


screen = Screen()
screen.exitonclick()