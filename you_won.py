from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")

class YouWon(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.hideturtle()

    def congrats(self):
        self.write("Congratulations! You beat all 10 levels!", False, align=ALIGNMENT, font=FONT)
