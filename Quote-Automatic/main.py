import requests
from tkinter import*
def get_quote():
    response = requests.get(url="http://api.kanye.rest")
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas.grid(column=0, row=0)
quote_text = canvas.create_text(150, 207,
                                text="Kanye Quote Goes Here",
                                width=250,
                                font=("Times", "20", "bold italic"),
                                fill="white")

baby_img = PhotoImage(file="baby.png")
baby_button = Button(image=baby_img, highlightthickness=0, command=get_quote)
baby_button.grid(column=0, row=1)





window.mainloop()