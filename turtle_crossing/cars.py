from turtle import Turtle
import random

colors=["red", "orange", "yellow", "green", "blue", "purple"]
x_cor=[220, -320]
class Cars():
    def __init__(self):
        self.all_cars=[]
        self.speed_car=5

    def generate_car(self):
        luck= random.randint(0,5)
        if(luck==3):
            car= Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.color(random.choice(colors))
            car.speed(6)
            y_cor= random.randint(-230,230)
            car.goto(x_cor[0],y_cor)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed_car)

    def update_speed(self):
        self.speed_car+=1