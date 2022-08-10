import tkinter as t
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = t.Tk()
        self.window.title("Quizzter")

        self.window.config(height=600, width=400, padx=50, pady=50, bg=THEME_COLOR)
        self.score_label = t.Label(text=f"Score: {self.quiz.score} / 10", font=("Arial", 16, "normal"), bg=THEME_COLOR,
                                   fg="white")
        self.canvas = t.Canvas(height=350, width=350, bg="white")
        self.text = self.canvas.create_text(175, 175, width=320,
                                            text="",
                                            font=("Arial", 16, "normal")
                                            )

        self.right_image = t.PhotoImage(file="images/true.png")
        self.right_button = t.Button(image=self.right_image, command=self.check_against_true)

        self.wrong_image = t.PhotoImage(file="images/false.png")
        self.wrong_button = t.Button(image=self.wrong_image, command=self.check_against_false)

        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        self.question_no = 0
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")
        if self.question_no < 10:
            self.question_no += 1
            self.canvas.itemconfig(self.text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.text, text=f"Score : {self.quiz.score} / 10")

    def check_against_true(self):
        answer = "True"
        result = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.quiz.score} / 10")
        self.feedback(result)

    def check_against_false(self):
        answer = "False"
        result = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.quiz.score} / 10")
        self.feedback(result)

    def feedback(self, is_true):
        if not is_true:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="light green")

        self.window.after(1000, self.get_next_question)

