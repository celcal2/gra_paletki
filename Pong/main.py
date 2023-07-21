from turtle import Screen
from bar import Bar
from ball import Ball
import time
from score import Score

game_is_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG Celina')

bar_right = Bar(350)
bar_left = Bar(-350)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(bar_right.go_up, "Up")
screen.onkey(bar_right.go_down, "Down")

screen.onkey(bar_left.go_up, "s")
screen.onkey(bar_left.go_down, "x")

while game_is_on:
    screen.update()
    ball.ball_move()

    # collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with a bar
    if ball.distance(bar_right) < 50 and ball.xcor() > 320 or ball.distance(bar_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect R bar miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score >=5 or score.r_score >=5:
        game_is_on = False
        score.goto(0, 0)
        score.write("Game Over", align='center', font=('Courier', 80, 'normal'))

screen.exitonclick()
