import colorgram
import turtle as tur
import random


img = input("Enter the location of the image : ")
num = int(input("Enter number of color to be extracted : "))

colors = colorgram.extract(img, num)
rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r, g, b))

h = int(input("Enter height of the painting : "))
b = int(input("Enter breadth of the painting : "))
size = int(input("Enter size of dots : "))
space = int(input("Enter the space between dots : "))

t = tur.Turtle()
sc = tur.Screen()
tur.colormode(255)
t.speed("fastest")

t.penup()
width = sc.window_width()
height = sc.window_height()
t.goto((-width / 2 + size), (height / 2 - size))
t.pendown()
t.setheading(0)
"""
- X = -width/2 → go all the way to the left edge. 
- Y = height/2 → go all the way to the top edge.
turle is in centre so as in graph we should move negative value in x and positive in y to go to left topmost corner

"""
t.hideturtle()


for i in range(h):
    for j in range(b):
        t.dot(size, random.choice(rgb))
        t.penup()
        t.forward(space)
        t.pendown()

    t.penup()
    t.setheading(270)
    t.forward(space)
    t.setheading(180)
    t.forward(space * b)
    t.setheading(0)
    t.pendown()

sc.exitonclick()
