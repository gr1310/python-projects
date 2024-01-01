from turtle import Turtle

TEXT_COLOR= "black"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup() 
        self.goto(0,270)   
        self.score=0
        self.speed("fastest")
        self.color(TEXT_COLOR)
        self.write(
            arg=f"Your Score is {self.score}",
            move=False,
            align="center",
            font=('Courier', 12, 'normal'),
        )
        

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(
            arg="Game Over!!",
            move=False,
            align="center",
            font=('Courier', 20, 'normal'),
        )
        self.goto(0,-40)
        self.color("black")
        self.write(
            arg="Press 'space bar' to restart the game",
            move=False,
            align="center",
            font=('Courier', 15, 'normal'),
        )

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(
            arg=f"Your Score is {self.score}",
            move=False,
            align="center",
            font=('Courier', 12, 'normal'),
        )