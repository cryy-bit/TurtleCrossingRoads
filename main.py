import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    if player.end():
      player.goback()
      car_manager.increment_speed()
      score.add_score()

    for cars_ in car_manager.all_cars:
      if player.distance(cars_)<20:
        score.you_lose_screen()
        game_is_on=False
    
