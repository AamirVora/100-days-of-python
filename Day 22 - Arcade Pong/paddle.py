from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.setposition(position)
        self.dx = 2

    def up(self):
        self.fd(20)

    def down(self):
        self.bk(20)



