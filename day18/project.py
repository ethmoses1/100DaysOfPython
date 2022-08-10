import colorgram
from turtle import Turtle, Screen
import turtle as t
from random import choice

t.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(245, 238, 238), (246, 244, 244), (202, 110, 110), (240, 241, 241), (236, 243, 243), (149, 50, 50), (222, 136, 136), (53, 123, 123), (170, 41, 41), (138, 20, 20), (134, 184, 184), (197, 73, 73), (47, 86, 86), (73, 35, 35), (145, 149, 149), (14, 70, 70), (232, 165, 165), (160, 158, 158), (54, 50, 50), (101, 77, 77), (183, 171, 171), (36, 74, 74), (19, 89, 89), (82, 129, 129), (147, 19, 19), (27, 102, 102), (12, 64, 64), (107, 153, 153), (176, 208, 208), (168, 102, 102)]

def horizontal():
    timmy_the_turtle.color(choice(color_list))
    for _ in range(1, 11):
        timmy_the_turtle.dot(20)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
        timmy_the_turtle.pendown()
        timmy_the_turtle.dot(20)
def vertical():
    timmy_the_turtle.speed("fastest")
    timmy_the_turtle.penup()
    
    for _ in range(1, 11):
        timmy_the_turtle.backward(50)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.right(90)
    timmy_the_turtle.pendown()
    
for v in range(1, 11):
    horizontal()
    vertical()


horizontal()
screen = Screen()
screen.exitonclick()
