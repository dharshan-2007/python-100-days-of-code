# Drawing Square

from turtle import Turtle, Screen

square = Turtle()
square.shape("square")
screen = Screen()
square.color("green")
for i in range(4):
    square.forward(150)
    square.right(90)
screen.exitonclick()
