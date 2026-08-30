from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.reinitiate()

    def reinitiate(self):
        x_loc = random.randint(-270, 270)
        y_loc = random.randint(-270, 270)
        self.goto(x_loc, y_loc)