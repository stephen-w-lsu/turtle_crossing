from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 280)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.setposition(POSITION)
        self.write_scoreboard()
        self.hideturtle()

    def increase_level(self):
        self.level += 1

    def write_scoreboard(self):
        self.write(f"Level {self.level}")

    def update_scoreboard(self):
        self.clear()
        self.write_scoreboard()
