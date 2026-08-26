import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finish_line import FinishLine

screen = Screen()

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
finish_line = FinishLine()

for _ in range(100):
    finish_line.custom_line()

screen.listen()

screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.drive_car()

    # Detect players collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    # Increase Score and Player Level up
    if player.ycor() > 200:
        player.player_reset()
        scoreboard.increase_score()
        car_manager.speed_up()

screen.exitonclick()





