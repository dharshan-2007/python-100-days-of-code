from turtle import Turtle, Screen


class draw:
    def draw_shape(self, sides, obj):
        angle = 360 / sides
        for i in range(sides):
            obj.forward(70)
            obj.right(angle)


shape = Turtle()
sc = Screen()

example = draw()
shape.color("blue")
example.draw_shape(3, shape)
shape.color("red")
example.draw_shape(4, shape)
shape.color("green")
example.draw_shape(5, shape)
shape.color("yellow")
example.draw_shape(6, shape)
shape.color("brown")
example.draw_shape(7, shape)
shape.color("violet")
example.draw_shape(8, shape)
shape.color("indigo")
example.draw_shape(9, shape)
shape.color("blue")
example.draw_shape(10, shape)

sc.exitonclick()
