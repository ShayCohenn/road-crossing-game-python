import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    # Initialize the screen
    screen = Screen()
    screen.clear()
    screen.title("Road Crossing Game")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Initialize objects
    cars = CarManager()
    player = Player()
    score = Scoreboard()

    # Key binds
    screen.listen()
    screen.onkeypress(player.move_forward, 'Up')
    screen.onkeypress(player.move_backwards, 'Down')
    screen.onkey(main, 'r')

    game_is_on = True
    while game_is_on:
        time.sleep(0.02)
        cars.move()

        # Detect collision between player and car
        for car in cars.cars:
            if car.distance(player) < 20:
                score.game_over()
                game_is_on = False

        # Detect player winning
        if player.ycor() > 280:
            player.reset_position()
            cars.level_up()
            score.increase_level()
        screen.update()

    screen.exitonclick()

if __name__ == '__main__':
    main()