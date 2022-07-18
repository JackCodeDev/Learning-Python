from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/list.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    current_card = {}


def remove_word():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    flip_timer = window.after(3000, flip_card)
    canvas.itemconfig(card_background, image=card_front)


def flip_card():
    canvas.itemconfig(card_title, text="Vietnamese", fill="pink")
    canvas.itemconfig(card_word, text=current_card["Vietnamese"], fill="pink")
    canvas.itemconfig(card_background, image=card_back)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=840, height=473)
card_front = PhotoImage(file="image-front.png")
card_back = PhotoImage(file="image-back.png")
card_background = canvas.create_image(400, 236, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(420, 140, text="", font=("Ariel", 40, "italic"), fill="white")
card_word = canvas.create_text(420, 260, text="", font=("Ariel", 60, "bold"), fill="white")
cancel_img = PhotoImage(file="cancel.png")
cancel_button = Button(image=cancel_img, command=next_card)
cancel_button.grid(row=1, column=0)

tick_img = PhotoImage(file="tick.png")
tick_button = Button(image=tick_img, command=remove_word)
tick_button.grid(row=1, column=1)

next_card()

window.mainloop()
