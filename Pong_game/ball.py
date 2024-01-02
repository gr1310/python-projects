from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.x_move= 10
        self.y_move= 10
        self.set_speed= 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move*=-1

    def bounce_other(self):
        self.x_move*=-1
        self.set_speed*=0.9
    
    # def increase_speed(self):
    #     self.set_speed*=0.9
        