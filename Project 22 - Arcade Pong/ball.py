from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1,1)
        self.dx = 1
        self.dy = 1

    def move(self):
        x_pos = self.xcor() + self.dx
        y_pos = self.ycor() + self.dy
        self.goto(x_pos,y_pos)


    def collision(self):
        self.dy *= -1

    def hit(self):
        self.dx *= -1

    def ball_reset(self):
        self.setposition(0,0)
        self.hit()

    def speed_increase(self):
        self.dx *= 1.2
        self.dy *= 1.2

    def speed_reset(self):
        self.dx = 1
        self.dy = 1


