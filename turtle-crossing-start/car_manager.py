from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed_car = STARTING_MOVE_DISTANCE
        # self.speed_all_car = 0.1

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_y = random.randint(-240, 240)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def refresh_car(self):
        self.all_cars = []

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed_car)

    def level_up(self):
        self.speed_car += MOVE_INCREMENT
        # self.speed_all_car *= 0.9

