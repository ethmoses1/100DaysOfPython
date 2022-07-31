#tutrle package
#Object oriented programming
# import turtle
# timmy = turtle.Turtle()



# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("CadetBlue")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


#prettytable package
from prettytable import PrettyTable
table  = PrettyTable()
table.add_column('Pokemon Name',["Pikachu", "Squirtle", "Charmander"])
table.add_column('Type',["Electric", "Water", "Fire"])
table.align = "l"

print(table)
