import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("AV's nake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtle_head.distance(food) < 15:
        food.reinitiate()
        snake.extend()
        scoreboard.increase_score()

    if snake.turtle_head.xcor() > 280 or snake.turtle_head.xcor() < -280 or snake.turtle_head.ycor() < -280 or snake.turtle_head.ycor() > 280:
        game_on = False
        turtle.color("white")
        turtle.write("Game Over", align="center", font=("Courier", 15, "normal"))

    for square in snake.squares:
        if square == snake.turtle_head:
            pass
        elif snake.turtle_head.distance(square) < 10:
            game_on = False
            turtle.color("white")
            turtle.write("Game Over", align="center", font=("Courier", 15, "normal"))


screen.exitonclick()

