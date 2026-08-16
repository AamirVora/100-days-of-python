from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

tim = Turtle()
screen = Screen()
ball = Ball()
score = Score()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("AV's Pong Game")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

screen.listen()

screen.onkeypress(l_paddle.up, "Up")
screen.onkeypress(l_paddle.down, "Down")
screen.onkeypress(r_paddle.up, "w")
screen.onkeypress(r_paddle.down, "s")


game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision()

    if ball.distance(r_paddle) < 50 and ball.xcor() < -330 or ball.distance(l_paddle) < 50 and ball.xcor() > 330:
        ball.hit()
        ball.speed_increase()

    if ball.xcor() > 400:
        ball.ball_reset()
        score.l_player_points()
        ball.speed_reset()


    if ball.xcor() < -400:
        ball.ball_reset()
        score.r_player_points()
        ball.speed_reset()

screen.exitonclick()