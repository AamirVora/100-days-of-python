from turtle import Screen,Turtle


tim = Turtle(shape="turtle")
tim.color("red")
screen = Screen()
screen.bgcolor("black")
tim.speed(3)

game_is_on = True


def right():
    tim.rt(90)


def up():
    tim.fd(90)


screen.listen()

while game_is_on:
    tim.penup()
    tim.fd(1)





    screen.onkeypress(right, "Right")
    screen.onkeypress(up, "Up")






screen.exitonclick()