
import turtle
import random
import tkinter.messagebox as msgbox

"""
turtle.textinput(title,promt)
turtle.numinput(title,promt)
used to show a popup and get input from the user
"""
sc=turtle.Screen()
sc.setup(width=500,height=400)
user_bet=sc.textinput(title="Make your bet",prompt="Which turtle will win the race..? Enter a color : (red, orange, Yellow, green, blue, purple)")
raceon=False

colors=["red","orange", "Yellow","green","blue","purple"]
ypos=[-70,-40,-10,20,50,80]
turtle_index=[]

for i in range(0,6):

    t=turtle.Turtle(shape="turtle")
    #or t.shape("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230,ypos[i])
    t.pendown()
    turtle_index.append(t)

if user_bet:
    raceon=True

while raceon:
    for tur in turtle_index:
        if tur.xcor()>230:
            winclr=tur.pencolor()
            if winclr==user_bet:
                msgbox.showinfo("Race results",f"You have won !! {winclr} is the winner")
            else:
                msgbox.showinfo("Race results",f"you have lost !! {winclr} is the winner")
            raceon=False
        ramdist=random.randint(0,15)
        tur.forward(ramdist)

sc.exitonclick()
