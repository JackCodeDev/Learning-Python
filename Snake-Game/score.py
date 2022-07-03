from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("deep pink")
        self.penup()
        self.goto((0, 270))
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f'Score: {self.score}', font=FONT, align=ALIGNMENT)

    def new_score(self):
        self.clear()
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over!', font=FONT, align=ALIGNMENT)






