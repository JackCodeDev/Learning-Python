from turtle import Turtle


class Wall:
    def __init__(self, x, y):
        self.wall = Turtle("square")
        self.wall.color("white")
        self.wall.shapesize(stretch_wid=1, stretch_len=40)
        self.wall.penup()
        self.wall.goto(x, y)
