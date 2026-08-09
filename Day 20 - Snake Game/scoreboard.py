from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-15,270)
        self.write(f"Score = {self.score}", move=False, align="center", font=("Times New Roman", 15, "bold"))


    def increase_score(self):

        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", move=False, align="center", font=("Times New Roman", 15, "bold"))
