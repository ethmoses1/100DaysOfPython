from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

cord = [{"x": -230, "y": -100}, 
               {"x": -230, "y": -60},
               {"x": -230, "y": -20},
               {"x": -230, "y": 20},
               {"x": -230, "y": 60},
               {"x": -230, "y": 100}, 
               ]

for position in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[position])
    new_turtle.penup()
    new_turtle.goto(x=cord[position]["x"], y=cord[position]["y"])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
    
screen.exitonclick()



