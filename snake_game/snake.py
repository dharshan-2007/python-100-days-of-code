from turtle import Turtle

class Snake:
    def __init(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        self.add_segment((0,0))

    def add_segment(self,position):
        new=Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.segments.append(new)

    def extend_segment(self)
        self.add_segment(self.segments[-1].position())

    def move(self):