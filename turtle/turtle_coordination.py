
import turtle
import random

"""
turtle.textinput(title,promt)
turtle.numinput(title,promt)
used to show a popup and get input from the user
"""
sc=turtle.Screen()
sc.setup(width=500,height=400)
user_bet=sc.textinput(title="Make your bet",prompt="Which turtle will win the race..? Enter a color : ")

colors=["red","orange", "Yellow","green","blue","purple"]


t=turtle.Turtle(shape="turtle")
#or t.shape("turtle")
t.penup()
t.goto(-230)
t.pendown()
sc.exitonclick()
