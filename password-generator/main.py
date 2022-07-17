from tkinter import*
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
FONT_NAME = "Courier"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
#################################PASSWORD-GENERATOR##########################


def password_generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(6, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


#################################DATA#########################################


def add_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"There are the detail entered: \nEmail: {email} "
                               f"\nPassword: {password} \nIs it ok save?")

        if is_okay:
            with open("data.txt", "a") as data:

                data.write("website: "+website+" | "+"Email/Username: "+email+" | "+"Password: "+password+"\n")
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                password_entry.delete(0, END)



##################################UI##########################################


window = Tk()
window.title("Generate Password")
window.config(padx=20, pady=20)
canvas = Canvas(width=300, height=300, highlightthickness=0)
new_img = PhotoImage(file="1.png")
canvas.create_image(150, 150, image=new_img)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:", fg="black", highlightthickness=0)
website_text.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2, row=1)

email_username_text = Label(text="Email/Username:", fg="black", highlightthickness=0)
email_username_text.grid(column=0, row=2)
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, columnspan=2, row=2)
email_username_entry.insert(0, "@gmail.com")

password_text = Label(text="Password:", fg="black", highlightthickness=0)
password_text.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_pw_button = Button(text="Generate Password", command=password_generate)
generate_pw_button.grid(column=3, row=2)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1, row=4)



canvas.mainloop()