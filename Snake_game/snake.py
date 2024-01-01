from turtle import Turtle
from turtle import *
import time

MOVE_STEPS= 20
START_COOR= [(20,0),(0,0),(-20,0)]
SNAKE_COLOR="black"

class Snake():
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head= self.segments[0]

    def createSnake(self):
        for i in range(-1,2,1):
            t=Turtle(shape="square")
            t.penup()
            t.goto(20*i,0)
            t.color(SNAKE_COLOR)
            self.segments.append(t)
        self.segments.reverse()
        # for i in range(3):
        #     t=Turtle(shape="square")
        #     t.penup()
        #     t.goto(START_COOR[i])
        #     t.color("white")
        #     self.segments.append(t)


    def updateNew(self):
        newPart= Turtle(shape="square")
        newPart.penup()
        newPart.color(SNAKE_COLOR)
        newPart.speed("fastest")
        originalHead= self.head.heading()
        if(originalHead==0):
            lastCor_x= self.segments[len(self.segments)-1].xcor()
            lastCor_y= self.segments[len(self.segments)-1].ycor()
            newPart.goto(lastCor_x-20,lastCor_y)
            self.segments.append(newPart)
        elif(originalHead==90):
            lastCor_x= self.segments[len(self.segments)-1].xcor()
            lastCor_y= self.segments[len(self.segments)-1].ycor()
            newPart.goto(lastCor_x,lastCor_y-20)
            self.segments.append(newPart)
        elif(originalHead==180):
            lastCor_x= self.segments[len(self.segments)-1].xcor()
            lastCor_y= self.segments[len(self.segments)-1].ycor()
            newPart.goto(lastCor_x+20,lastCor_y)
            self.segments.append(newPart)
        elif(originalHead==270):
            lastCor_x= self.segments[len(self.segments)-1].xcor()
            lastCor_y= self.segments[len(self.segments)-1].ycor()
            newPart.goto(lastCor_x,lastCor_y+20)
            self.segments.append(newPart)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            x= self.segments[seg-1].xcor()
            y= self.segments[seg-1].ycor()
            self.segments[seg].goto(x,y)
        self.segments[0].forward(20)
        # for i in self.segments:
        #     print(i.xcor(),i.ycor())
        # print("------------")

    def up(self):
        if(self.segments[0].heading()!=270):
            self.segments[0].setheading(90)

    def left(self):
        if(self.segments[0].heading()!=0):
            self.segments[0].setheading(180)
    def down(self):
        if(self.segments[0].heading()!=90):
            self.segments[0].setheading(270)

    def right(self):
        if(self.segments[0].heading()!=180):
            self.segments[0].setheading(0)