COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

from turtle import Turtle
import random

class CarManager:
    def __init__(self):

        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        car_control = random.randint(1, 6)
        if car_control == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            y = random.randint(-250,200)
            new_car.goto(300,y)
            self.cars.append(new_car)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def drive_car(self):
        for car in self.cars:
            car.fd(self.car_speed)


