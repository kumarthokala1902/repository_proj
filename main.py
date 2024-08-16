from turtle import Turtle, Screen
from pane import Pane
from ball import Ball
import time
from scoreboard import Scoreboard


turtle = Turtle()
screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pang game")

r_pane = Pane((370,0))
l_pane = Pane((-380,0))


screen.listen()
screen.onkey(r_pane.go_up, "Up")
screen.onkey(r_pane.go_down,"Down")
screen.onkey(l_pane.go_up, "r")
screen.onkey(l_pane.go_down,"w")
ball = Ball()
score = Scoreboard()
# ball_listen.ball_move()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()


    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce_y()

    if ball.distance(r_pane) < 50 and ball.xcor() > 340:

        ball.bounce_x()
    if ball.distance(l_pane) < 50 and ball.xcor() < -340:
        ball.bounce_xx()
    if ball.xcor() > 380:
        ball.ball_reset_xx()
        score.l_point()

    if ball.xcor() < -380:
        ball.ball_reset_xx()
        score.r_point()




screen.exitonclick()