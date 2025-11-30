from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    """Manages creation, movement and cleanup of car turtles."""
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create a car at the right edge."""
        # 1-in-6 chance to create a car each tick
        ran = random.randint(1, 6)
        if ran == 1:
            new = Turtle("square")
            new.shapesize(stretch_len=2, stretch_wid=1)
            new.color(random.choice(COLORS))
            new.penup()
            random_y = random.randint(-250, 250)
            new.goto(320, random_y)
            new.setheading(180)
            self.all_cars.append(new)

    def move_cars(self):
        """Move all cars left and remove those that are off-screen."""
        for car in self.all_cars[:]:
            car.forward(self.car_speed)
            # remove car if it moved off the left edge
            if car.xcor() < -340:
                car.hideturtle()
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT