from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-240,270)
        self.level=0
        self.write(f"Level {self.level}", align="center", font=("Courier",15,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER",align="center", font=("Courier",20,"normal"))
    
    def update_level(self):
        self.goto(-240,270)
        self.clear()
        self.level+=1
        self.write(f"Level {self.level}", align="center", font=("Courier",15,"normal"))