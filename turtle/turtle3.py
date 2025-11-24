from turtle import Turtle as t,Screen as s
draw=t()
sc=s()
for _ in range(20):
    draw.forward(15)
    draw.penup()
    draw.forward(15)
    draw.pendown()
sc.exitonclick()