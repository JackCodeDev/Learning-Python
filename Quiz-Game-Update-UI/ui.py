from tkinter import*
from quiz import QuizBrain
THEME_COLOR = "#375362"


class UiInterface:
    def __init__(self, q_bank: QuizBrain):
        self.quiz = q_bank
        self.window = Tk()
        self.window.title("Quiz-Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some Question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        tick_img = PhotoImage(file="tick.png")
        self.tick_button = Button(image=tick_img, highlightthickness=0, command=self.true_pressed)
        self.tick_button.grid(column=1, row=2)

        cross_img = PhotoImage(file="cross.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(column=0, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():

            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of question.")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


