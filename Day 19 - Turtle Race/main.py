"""
Day 19 - Sketcheritch Project"""

# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.color("green")
# tim.shape("turtle")
# screen = Screen()
# screen.bgcolor("black")
#
#
# def forward():
#     tim.forward(20)
#
# def backward():
#     tim.backward(20)
#
# def left():
#     tim.left(10)
#
# def right():
#     tim.right(10)
#
# def clear_screen():
#     tim.clear()
#     tim.up()
#     tim.home()
#     tim.down()
#
#
# screen.onkey(forward, "Up")
# screen.onkey(backward, "Down")
# screen.onkey(left, "Left")
# screen.onkey(right, "Right")
# screen.onkey(clear_screen, "c")
# screen.listen()
#
# screen.exitonclick()


"""Turtle Race Project"""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
y_pos = [0, 50, 100, 150, -50, -100, -150]

race_on = True


for turtle in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-250, y_pos[turtle])
    all_turtles.append(new_turtle)

user_bet = screen.textinput("Bet On", "Choose Turtle color")
screen.title("Turtle Race Project")
while race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You've won! Your {user_bet} turtle wins!")
            else:
                print(f"Your {user_bet} turtle lost!")

        fd_distance = random.randint(0, 10)
        turtle.forward(fd_distance)




screen.exitonclick()


