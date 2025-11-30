from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        start_positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in start_positions:
            self.add_segment(pos)

    def add_segment(self,position):
        new=Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.segments.append(new)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)