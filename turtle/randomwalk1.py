import turtle as t
import random
from turtle import Screen

def randomColor():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    return red,green,blue

sc=Screen()
tim=t.Turtle()
t.colormode(255)

directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(random.randrange(150,250)):
    tim.color(randomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))
sc.exitonclick()