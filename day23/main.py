import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import choice

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.move_cars()
    car.create_car()
    
    #Detect if car has reached top wall
    if player.ycor() > 300:
        scoreboard.update_level()
        player.goto_starting_pos()
        car.level_up()
    
    #Detect collision with a car
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
        
screen.exitonclick()