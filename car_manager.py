from turtle import Turtle
import random

COLORS = ["red", "orange", "pink", "brown", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
CAR_AMOUNT = 10

class CarManager(Turtle):
    
    def __init__(self):
        self.cars = []
        self.xspeed = STARTING_MOVE_DISTANCE
        self.car_amount = CAR_AMOUNT
        for _ in range(self.car_amount):
            self.add_car()

    def add_car(self):
        """Create a new car and append it to the cars list
        Give it a random color from the colors list and set its position
        for a random value between -300 and 300 on the x axis and random value for
        the y axis between -250 and 250 to give it some space on the top and bottom"""
        new_car = Turtle(shape='square')
        new_car.penup()
        new_car.shapesize(1,2)
        new_car.seth(180)
        new_car.color(random.choice(COLORS))
        new_car.goto(random.randint(-300,300),random.randint(-250,250))
        self.cars.append(new_car)

    def move(self):
        """Move each car forward and make them loop around"""
        for car in self.cars:
            car.forward(self.xspeed)
            if car.xcor() < -320:
                car.goto(300, car.ycor())

    def level_up(self):
        """When leveling up make the cars go faster and add a new car"""
        self.xspeed += 0.1
        self.add_car()