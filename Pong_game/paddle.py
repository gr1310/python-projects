from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4.5, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(350,0)
        self.color("white")

    def move_down(self):
        x_cor= self.xcor()
        y_cor= self.ycor()-20
        self.goto(x_cor,y_cor)
    def move_up(self):
        x_cor= self.xcor()
        y_cor= self.ycor()+20
        self.goto(x_cor,y_cor)