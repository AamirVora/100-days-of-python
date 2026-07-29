import turtle
from turtle import Screen, Turtle
import random



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("chartreuse")
tim.speed("fastest")


def draw_offset(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)

draw_offset(5)

screen = Screen()
screen.bgcolor("black")
screen.exitonclick()










#
#
#
# up = tim.forward
# down = tim.backward
# left = tim.left
# right = tim.right
#
# directions_move = [up, down]
# directions_turn = [left, right]
# screen = Screen()
# screen.bgcolor("black")
#
# for _ in range(200):
#     colors = random_color()
#     tim.pencolor(colors)
#     tim.pensize(10)
#     tim.speed(5)
#     move = random.choice(directions_move)
#     turn = random.choice(directions_turn)
#     move(50)
#     turn(90)
#
# screen.exitonclick()








