from turtle import Turtle


class Snake:

    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_SPEED = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.turtle_head = self.squares[0]


    def create_snake(self):
        for position in self.STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square_1 = Turtle(shape="square")
        square_1.color("white")
        square_1.penup()
        square_1.goto(position)
        self.squares.append(square_1)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for square in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[square -1].xcor()
            new_y = self.squares[square -1].ycor()
            self.squares[square].goto(new_x, new_y)

        self.turtle_head.fd(self.MOVE_SPEED)

    def reset(self):
        for square in self.squares:
            square.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.turtle_head = self.squares[0]


    def up(self):
        if self.turtle_head.heading() != self.DOWN:
            self.turtle_head.setheading(90)

    def down(self):
        if self.turtle_head.heading() != self.UP:
            self.turtle_head.setheading(270)

    def left(self):
        if self.turtle_head.heading() != self.RIGHT:
            self.turtle_head.setheading(180)

    def right(self):
        if self.turtle_head.heading() != self.LEFT:
            self.squares[0].setheading(0)


