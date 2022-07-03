from turtle import Turtle
START_POSITION_1 = [(350, 0)]
START_POSITION_2 = [(580, 20), (580, 0), (580, -20)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle:
    def __init__(self, x, y):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_left(self):
        new_x = self.paddle.xcor() - 20
        self.paddle.goto(new_x, self.paddle.ycor())

    def go_right(self):
        new_x = self.paddle.xcor() + 20
        self.paddle.goto(new_x, self.paddle.ycor())



    # def left(self):
    #     if self.paddle_head.heading() != RIGHT:
    #         self.paddle_head.setheading(180)
    #
    # def right(self):
    #     if self.paddle_head.heading() != LEFT:
    #         self.paddle_head.setheading(0)

