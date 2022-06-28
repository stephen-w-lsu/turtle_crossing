from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_CAR_AMT = 1000


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2)
        self.penup()
        self.setposition(350, 0)
        self.setheading(180)

    def create_car(self):
        pass

    # Place cars randomly off-screen on the right
    def car_to_screen(self):
        self.setposition(random.randint(320, 100000), random.randint(-240, 260))

    def move(self):
        self.forward(MOVE_INCREMENT)
