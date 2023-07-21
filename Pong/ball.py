from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 3
        self.y_move = 3
        self.speed_up = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.speed_up *= 0.5

    def bounce_x(self):
        self.x_move *= -1
        self.speed_up *= 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.speed_up = 0.1
        self.bounce_x()




