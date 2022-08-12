from cgitb import text
from math import floor
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=70, pady=50)


miles_input = Entry(width=10)
miles_input.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=1)

km_label = Label(text=0)
km_label.grid(column=2, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)


def calculate():
    result = floor(float(miles_input.get())*1.609344)
    km_label.config(text=result)

button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=2)

window.mainloop()