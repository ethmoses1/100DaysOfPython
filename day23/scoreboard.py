from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.goto(-230, 260)
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.penup()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

    
