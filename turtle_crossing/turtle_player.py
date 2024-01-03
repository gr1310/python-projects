from turtle import Turtle

class Turtle_player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def move_forward(self):
        self.goto(self.xcor(),self.ycor()+20)
    
    def restart(self):
        self.goto(0,-280)
        self.setheading(90)
        