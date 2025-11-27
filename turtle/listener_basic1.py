import turtle

t=turtle.Turtle()
sc=turtle.Screen()

def moveforward():
    t.forward(10)
sc.listen()
sc.onkey(key="space",fun=moveforward)  # makes turtle to move forward when space bar is

sc.exitonclick()