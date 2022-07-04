from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.new_score()

    def update(self):
        self.clear()
        self.color("deep pink")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", font=FONT, align="left")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")

    def new_score(self):
        self.update()
        self.score += 1


