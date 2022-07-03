from turtle import Turtle
import random
from wall import Wall

START_LINE_POSITION = [(-10, -280), (-10, -240), (-10, -200), (-10, -160), (-10, -120), (-10, -80), (-10, -40),
                       (-10, 0), (-10, 40), (-10, 80), (-10, 120), (-10, 160), (-10, 200), (-10, 240), (-10, 280)]
DIRECTOR = (0, 360)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.line_body = []
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_ball = 10
        self.y_ball = 10
        self.move_speed = 0.1
        self.line = Turtle("square")
        self.line.shapesize(2)
        self.create_line()

    def create_line(self):
        for pad_position in START_LINE_POSITION:
            new_line_part = Turtle("square")
            new_line_part.color("white")
            new_line_part.penup()
            new_line_part.goto(pad_position)
            self.line_body.append(new_line_part)

    # def move_ball(self):
    #     self.ball.forward(20)

    def bounce_y(self):
        self.y_ball *= -1

    def bounce_x(self):
        self.x_ball *= -1
        self.move_speed *= 0.9

    def move_ball(self):
        x_ball = self.xcor() + self.x_ball
        y_ball = self.ycor() + self.y_ball
        self.goto(x_ball, y_ball)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
