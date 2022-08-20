from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Courier", 24, "italic")
class QuizInterface:
    def __init__(self, questions):
        self.quiz = QuizBrain(questions)
        self.window  = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20)
        
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, pady=20)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125, text=self.quiz.next_question(), font=("Arial", 20, "italic"), fill="black", width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

       
        rigth_image = PhotoImage(file="./images/true.png")
        self.right = Button(image=rigth_image, border=0, command=self.right)
        self.right.grid(column=0, row=2, pady=20)
        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=wrong_image, border=0, command=self.wrong)
        self.wrong.grid(column=1, row=2, pady=20)

        
        self.window.mainloop()
    
    def right(self):
        self.quiz.check_answer("True") 
        self.right_wrong()

    
    def wrong(self):
        self.quiz.check_answer("False")
        self.right_wrong()
        
    def change_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.question_number < 10:
            self.canvas.itemconfig(self.q_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.q_text, text=f"You got {self.quiz.score}/{self.quiz.question_number} correct")
    
    def right_wrong(self):
        if self.quiz.correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.change_question)