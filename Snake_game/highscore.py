from turtle import Turtle

TEXT_COLOR= "blue"

class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color(TEXT_COLOR)
        self.goto(200,270)
        self.highest_score=0
        self.write(
            arg=f"Highest Score is {self.highest_score}",
            move=False,
            align="center",
            font=('Courier', 12, 'normal'),
        )
    def printing(self):
        self.clear()
        self.write(
            arg=f"Highest Score is {self.highest_score}",
            move=False,
            align="center",
            font=('Courier', 12, 'normal'),
        )