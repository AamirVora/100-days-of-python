import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
#
# import colorgram
#
# colors = colorgram.extract('image.jpg', 10)
#
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb_color = (r,g,b)
#     rgb_color.append(new_rgb_color)
#
# print(rgb_color)
color_list = [(199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 104, 56), (5, 57, 83), (200, 216, 204), (108, 67, 85)]

tim = Turtle()
tim.color("green")
tim.penup()
tim.hideturtle()
tim.teleport(-350,-350)
tim.pendown()
tim.speed("fastest")

def move_pen():
    for _ in range(10):
        # tim.begin_fill()
        # tim.fillcolor(random.choice(color_list))
        # tim.circle(20)
        # tim.end_fill()
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()


screen = Screen()
screen.bgcolor("black")

for _ in range(10):
    move_pen()
    current_pos = tim.pos()
    new_x = current_pos[0]
    new_y = current_pos[1]
    new_pos = (-350, new_y - -50)
    tim.penup()
    tim.setpos(new_pos)








