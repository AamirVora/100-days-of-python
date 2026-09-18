FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,240)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)


