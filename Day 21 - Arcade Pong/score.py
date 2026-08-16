from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_player_score = 0
        self.r_player_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0,230)
        self.write(f"{self.l_player_score} Score {self.r_player_score}", font=("Courier", 40, "normal"), align = "Center")

    def l_player_points(self):
        self.clear()
        self.l_player_score += 1
        self.write(f"{self.l_player_score} Score {self.r_player_score}", font=("Courier", 40, "normal"), align = "Center")

    def r_player_points(self):
        self.clear()
        self.r_player_score += 1
        self.write(f"{self.l_player_score} Score {self.r_player_score}", font=("Courier", 40, "normal"), align = "Center")

