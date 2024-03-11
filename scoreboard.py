from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_text()

    def update_text(self):
        """Update the text"""
        self.clear()
        self.goto(0,250)
        self.write(f"Level {self.level}", align="center",move=True,font=FONT)

    def increase_level(self):
        """When a player levels up increase the level by 1 and update the text"""
        self.level += 1
        self.update_text()

    def game_over(self):
        """Write game-over text"""
        self.goto(0,0)
        self.write("Game Over, Press 'R' to restart", align="center",move=True,font=FONT)