from turtle import Turtle


class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=0.2)
        self.goto(-300,200)

    def custom_line(self):
        self.pendown()
        self.fd(5)
        self.penup()
        self.fd(5)
