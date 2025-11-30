from turtle import Turtle

STARTING_POSITION=(0,-200)
MOVE_DISTANCE=10
FINISH_LINE=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        return self.ycor()>FINISH_LINE
