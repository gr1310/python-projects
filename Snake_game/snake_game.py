from turtle import Screen
import time
from snake import *
from food import Food
import random 
from scoreboard import ScoreBoard
from highscore import HighScore

"""
Rules:
Snake size increases on getting food 
Game gets over if snake collides with itself or with the walls
Score increases as the snake eats food
To refresh the game after gameover press "Space"

"""

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("My Snake Game")


new_Snake= Snake()
food= Food()
score= ScoreBoard()
highest_src=0
hscr= HighScore()

screen.listen()
screen.onkey(new_Snake.up,"Up")
screen.onkey(new_Snake.down,"Down")
screen.onkey(new_Snake.left,"Left")
screen.onkey(new_Snake.right,"Right")



game_on=True


def gameStart(game_on,new_Snake,food,score, highest_src,hscr):
    # global highest_src
    while(game_on):
        screen.update()
        # hscr.printing()

        # Checking collision with the food - increases score and snake size

        if(food.distance(new_Snake.head.xcor(),new_Snake.head.ycor())<15):
            score.update_score()
            highest_src=max(highest_src, score.score)
            hscr.highest_score= highest_src
            hscr.printing()
            random_x= random.randint(-260,260)
            random_y= random.randint(-260,260)
            food.goto(random_x,random_y)
            new_Snake.updateNew()

        # Checking collision with the wall - ends the game
        
        if(new_Snake.head.ycor()>=280 or new_Snake.head.ycor()<=-280 or new_Snake.head.xcor()>=280 or new_Snake.head.xcor()<=-280):
            score.game_over()
            game_on=False

    # Checking collision with tail - ends the game
        
        for seg in new_Snake.segments[1:]:
            if(new_Snake.head.distance(seg)<10):
                score.game_over()
                game_on=False
        
    
        new_Snake.move()
    
if(game_on):
    gameStart(game_on,new_Snake,food,score, highest_src,hscr)

def refresh():
    high= hscr.highest_score
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("green")
    screen.title("My Snake Game")
    new_Snake=Snake()
    food= Food()
    score= ScoreBoard()
    hscr.printing()
    screen.listen()
    screen.onkey(new_Snake.up,"Up")
    screen.onkey(new_Snake.down,"Down")
    screen.onkey(new_Snake.left,"Left")
    screen.onkey(new_Snake.right,"Right")
    game_on=True
    gameStart(game_on,new_Snake,food,score, high,hscr)
    screen.onkey(refresh,"space")

screen.onkey(refresh,"space")

screen.exitonclick()
