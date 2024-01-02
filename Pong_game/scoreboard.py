from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score= 0
        self.r_score= 0
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=('Courier', 30, 'normal'))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=('Courier', 30, 'normal'))
    
    def write_score(self):
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=('Courier', 30, 'normal'))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=('Courier', 30, 'normal'))
    
    def update_l(self):
        self.l_score+=1
        self.clear()
        self.write_score()
    
    def update_r(self):
        self.r_score+=1
        self.clear()
        self.write_score()
