from turtle import Turtle, Screen

tom_the_turtle = Turtle()
tom_the_turtle.shape("arrow")

for _ in range(15):
    tom_the_turtle.forward(10)
    tom_the_turtle.penup()
    tom_the_turtle.forward(10)
    tom_the_turtle.pendown()




screen = Screen()
screen.exitonclick()