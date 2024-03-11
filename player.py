from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.seth(90)

    def move_forward(self):
        """Move the player forward by a specific amount"""
        self.forward(MOVE_DISTANCE)

    def move_backwards(self):
        """Move the player backwards by a specific amount"""
        if self.ycor() > -290:
            self.backward(MOVE_DISTANCE)

    def reset_position(self):
        """Reset the position of the player when going to a new level"""
        self.goto(STARTING_POSITION)
