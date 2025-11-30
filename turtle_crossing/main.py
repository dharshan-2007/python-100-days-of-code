from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(600,600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for c in car_manager.all_cars:
        if c.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    if player.is_finished():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()