from turtle import Screen
from turtle_player import Turtle_player
from cars import Cars
from score import ScoreBoard
import time

screen= Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player= Turtle_player()
car= Cars()
score_board= ScoreBoard()

screen.listen()
screen.onkeypress(player.move_forward,"Up")

game_on= True
while(game_on):
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move()
    for new_car in car.all_cars:
        if(player.distance(new_car)<23):
            game_on=False
            score_board.game_over()

    if(player.xcor()==0 and player.ycor()>=280):
        score_board.update_level()
        player.restart()
        car.update_speed()
   
screen.exitonclick()