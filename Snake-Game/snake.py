from turtle import Turtle
from score import Score

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def create_snake(self):
        for body_position in START_POSITION:
            self.add_body(body_position)

    def add_body(self, body_position):
        new_snake_part = Turtle("square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(body_position)
        self.snake_body.append(new_snake_part)

    def extend_body(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for segment_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_num - 1].xcor()
            new_y = self.snake_body[segment_num - 1].ycor()
            self.snake_body[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)




