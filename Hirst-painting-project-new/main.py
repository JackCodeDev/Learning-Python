from random import randint, choice
from turtle import Turtle, Screen

colors_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50),
               (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
               (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
               (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
               (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

timmy = Turtle()
screen = Screen()
timmy.shape("circle")
timmy.color("red")
timmy.pensize(1)
timmy.speed(20)
screen.colormode(255)

a = [0, 90, 180, 270]

n = 0
direction = [0, 90, 180, 270]
timmy.hideturtle()
timmy.left(225)
timmy.up()
timmy.forward(500)
timmy.right(225)
while n < 10:

    timmy.left(90)
    timmy.up()
    timmy.forward(50)
    timmy.right(90)
    for i in range(10):
        timmy.up()
        timmy.forward(50)
        timmy.down()
        timmy.dot(20)
        # timmy.right(choice(direction))
        timmy.color(choice(colors_list))
        # timmy.color((randint(0, 225), randint(0, 225), randint(0, 225)))
    timmy.up()
    timmy.backward(500)
    n += 1
timmy.forward(50)








screen.exitonclick()