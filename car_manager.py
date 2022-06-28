from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_CAR_AMT = 1000


class CarManager:

    def __init__(self):
        self.car_list = []

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.setposition(300, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)
