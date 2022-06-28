from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.setposition(0, 0)
        self.hideturtle()

    def game_over(self):
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

