from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle1= Paddle()
paddle2= Paddle()
paddle2.goto(-350,0)

scoreboard= ScoreBoard()
ball= Ball()

screen.listen()
screen.onkeypress(paddle1.move_down,"Down")
screen.onkeypress(paddle1.move_up,"Up")
screen.onkeypress(paddle2.move_down,"s")
screen.onkeypress(paddle2.move_up,"w")
# screen.tracer(1)


game_on= True
while game_on:
    time.sleep(ball.set_speed)
    # time.sleep(0.01)
    screen.update()
    ball.move()
    if(ball.ycor()>=280 or ball.ycor()<=-280):
        ball.bounce()

    if((paddle1.xcor()-ball.xcor())<=25 and ((ball.ycor()<=paddle1.ycor()+50 and ball.ycor()>=paddle1.ycor()) or (ball.ycor()>=paddle1.ycor()-50 and ball.ycor()<=paddle1.ycor()))):
        ball.bounce_other()
        # ball.increase_speed()
        
    elif(ball.xcor()>=360):
        scoreboard.update_l()
        ball.goto(0,0)
        ball.set_speed=0.1
        ball.y_move=10
        ball.x_move=-10

    if((paddle2.xcor()-ball.xcor())>=-25 and ((ball.ycor()<=paddle2.ycor()+50 and ball.ycor()>=paddle2.ycor()) or (ball.ycor()>=paddle2.ycor()-50 and ball.ycor()<=paddle2.ycor()))):
        ball.bounce_other()
        # ball.increase_speed()
    
    elif(ball.xcor()<=-360):
        scoreboard.update_r()
        ball.goto(0,0)
        ball.set_speed=0.1
        ball.y_move=10
        ball.x_move=10
screen.exitonclick()