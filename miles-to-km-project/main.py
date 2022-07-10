import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=300)
window.config(padx=20, pady=20)
# Label

my_label_Miles = tkinter.Label(text=" Miles")
my_label_Miles.grid(column=2, row=0)
my_label_Miles.config(padx=20, pady=20)

my_label_Km = tkinter.Label(text=" Km")
my_label_Km.grid(column=2, row=1)
my_label_Km.config(padx=20, pady=20)

my_label_is_equal_to = tkinter.Label(text=" is equal to")
my_label_is_equal_to.grid(column=0, row=1)
my_label_is_equal_to.config(padx=20, pady=20)

my_label_result = tkinter.Label(text="0")
my_label_result.grid(column=1, row=1)
my_label_result.config(padx=20, pady=20)

# Button


def miles_to_km():
    new_result = float(input_num.get())*1.60934
    my_label_result.config(text=new_result)


my_button_calculate = tkinter.Button(text="Calculate", command=miles_to_km)
my_button_calculate.grid(column=1, row=2)
my_button_calculate.config(padx=10, pady=10)

# Entry
input_num = tkinter.Entry(width=20)
input_num.get()
input_num.grid(column=1, row=0)

window.mainloop()
