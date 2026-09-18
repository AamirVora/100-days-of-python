from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f"Score: {self.score}/50", font=("Arial", 20, "normal"), align="center")


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}/50", font=("Arial", 20, "normal"), align="center")


