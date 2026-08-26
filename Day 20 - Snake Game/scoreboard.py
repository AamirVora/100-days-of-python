from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_high_score = open("data.txt", "r")
        self.high_score = self.update_high_score.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-15,270)
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.high_score_storage()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.high_score}", move=False, align="center",
                   font=("Times New Roman", 15, "bold"))

    def high_score_storage(self):
        file = open("data.txt", "w")
        file.write(f"{self.high_score}")
