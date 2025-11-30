from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)

ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True
while game_on:
    # move the ball, then update the screen and sleep
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # collision with paddles (explicit x/y checks for reliability)
    # right paddle
    if ball.xcor() > 320 and abs(ball.ycor() - r_paddle.ycor()) < 50:
        ball.bounce_x()
    # left paddle
    if ball.xcor() < -320 and abs(ball.ycor() - l_paddle.ycor()) < 50:
        ball.bounce_x()

    #r paddle misses ball
    if ball.xcor()>380:
        ball.reset_position() 
        scoreboard.l_point()

    #l paddle misses ball
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()