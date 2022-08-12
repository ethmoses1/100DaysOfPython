from cProfile import label
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)



#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

#change label
my_label["text"] = "New text"

#or

my_label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")

def change_label():
    my_label.config(text="MY LABEL")

    
# button = Button(text="click me", command=change_label)
# button.pack()

#Entry
def change_label_again():
    new_text = input.get()
    my_label.config(text=new_text)
    
button1 = Button(text="click me", command=change_label_again)
button1.grid(column=1, row=1)

button2 = Button(text="New Button", command=change_label_again)
button2.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)







window.mainloop() 