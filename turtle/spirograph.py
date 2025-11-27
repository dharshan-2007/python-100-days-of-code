import turtle as tur
import random

t=tur.Turtle()
tur.colormode(255)
sc=tur.Screen()

def randomColor():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    return red,green,blue

t.speed("fastest")
def drawSpirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        t.color(randomColor())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)

n=int(input("Enter size of gaps : "))
drawSpirograph(n)
sc.exitonclick()