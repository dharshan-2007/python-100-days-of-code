import turtle

print("w - move forward")
print("s - move backward")
print("a - turn left")
print("d - turn right")
print("c - clear")

t = turtle.Turtle()
sc = turtle.Screen()


def moveforward():
    t.forward(10)


def movebackward():
    t.backward(10)


def turnleft():
    t.left(90)


def turnright():
    t.right(90)


def clear():
    t.clear()
    t.penup()
    t.home()  # moves the turtle to the origin
    t.pendown()


sc.listen()
sc.onkey(moveforward, "w")
sc.onkey(movebackward, "s")
sc.onkey(turnleft, "a")
sc.onkey(turnright, "d")
sc.onkey(clear, "c")

sc.exitonclick()
