from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 40, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color("deep pink")
        self.penup()
        self.goto((-10, 200))
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f'{self.score_1}   {self.score_2}', font=FONT, align=ALIGNMENT)

    def new_score_1(self):
        self.clear()
        self.score_1 += 1
        self.update_score_board()

    def new_score_2(self):
        self.clear()
        self.score_2 += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over!', font=FONT, align=ALIGNMENT)

