#random walk
import turtle as t
import random
from turtle import Screen
sc=Screen()

t.colormode(255)
random_walk=t.Turtle()
directions=[0,90,180,270]
colors = [
    "deep pink",
    "medium sea green",
    "gold",
    "slate blue",
    "orange red",
    "turquoise",
    "orchid",
    "dark violet",
    "light coral",
    "spring green"
]

random_walk.pensize(15)

random_walk.speed("fastest")
'''
turtle.speed()
to set speed of the turtle
-"fastest" :0
-"fast" :10
-"normal" :6
-"slow" :3
-"slowest":1
'''
for _ in range(random.randrange(100,250)):
    random_walk.color(random.choice(colors))
    random_walk.forward(30)
    random_walk.setheading(random.choice(directions))

sc.exitonclick()