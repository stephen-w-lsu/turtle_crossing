
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from game_over import GameOver
from you_won import YouWon

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
time_sleep = 0.1
FINISH_LINE_Y = 280
player = Player()
scoreboard = Scoreboard()
game_over = GameOver()
you_won = YouWon()

# Create a 10K of cars
car_list = []
for _ in range(1000):
    car = CarManager()
    car_list.append(car)
    car.car_to_screen()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()

    # Keeps car continuously moving from right to left
    # Print game over if car collides with player
    for a_car in car_list:
        a_car.move()
        if a_car.distance(player.position()) < 20:
            game_over.game_over()
            game_is_on = False

    # Increase level and car speed each time player reaches goal
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        time_sleep *= 0.8

    # Print congratulations on screen when player finishes 10 levels
    if scoreboard.level == 10:
        you_won.congrats()
        game_is_on = False

screen.exitonclick()
