"""Reference
https://docs.python.org/3/library/turtle.html
"""

from turtle import Turtle, Screen

graph = Turtle()
graph.shape("turtle")

graph.shape("arrow")  # Default shape, looks like a triangle pointing forward
graph.shape("turtle")  # A cute turtle icon
graph.shape("circle")  # A simple circle
graph.shape("square")  # A square shape
graph.shape("triangle")  # An equilateral triangle
graph.shape("classic")  # The original turtle shape (like a small triangle)

# For colors https://cs111.wellesley.edu/reference/colors
graph.color("red")
graph.forward(100)
graph.right(90)
graph.forward(100)
graph.left(180)
graph.forward(100)
graph.left(90)
graph.forward(100)

screen = Screen()
# screen.exitonclick()  #Will exit the window after clicking
