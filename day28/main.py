from cgitb import text
from curses import window
from tkinter import *
import math
from pygame import mixer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
mixer.init()

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def play():
    mixer.music.load("sunset_countdown_timer.mp3")
    mixer.music.set_volume(0.8)
    mixer.music.play()
    
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    if reps ==8:
        count_down(long_break_sec)
        top_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        top_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        top_label.config(text="Work", fg=GREEN)
        
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
     
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

import time

# ---------------------------- UI SETUP ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        play()
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check_marks.config(text=mark)
            
        
        
window = Tk()
window.title('Pomodoro')
window.config(padx=200, pady=50, bg=YELLOW)

top_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
top_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="start", highlightbackground = YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="reset", highlightbackground = YELLOW, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_marks.grid(column=1, row=3)
window.mainloop()

