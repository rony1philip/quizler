from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain, question: Question):
        self.question_data_level_2 = None
        self.question_data_level_3 = None
        self.question = question
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.window.minsize(width=500, height=615)

        self.canvas = Canvas(width=500, height=450, bg=THEME_COLOR)
        image = PhotoImage(file="C:/Users/user/PycharmProjects/quizzier-app/images/text_books.png")
        self.canvas.create_image(253, 225, image=image)
        self.question_text = self.canvas.create_text(253, 225, width=320, text='', fill='white',
                                                     font=('Courier', 18, 'bold'))
        self.canvas.grid(column=1, row=2, columnspan=2)

        self.score_bord = Label(width=15, text=f'score:{self.score}', fg=THEME_COLOR, font=('Courier', 18, 'bold'))
        self.score_bord.grid(column=2, row=1)

        t_image = PhotoImage(file='images/true.png')
        self.true = Button(image=t_image, highlightthickness=0, command=self.v_button)
        self.true.place(x=115, y=470)

        f_image = PhotoImage(file='images/false.png')
        self.true = Button(image=f_image, highlightthickness=0, command=self.x_button)
        self.true.place(x=285, y=470)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(highlightbackground='white', highlightthickness=2)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        elif self.quiz.question_number_t == 30:
            q_text = 'finito'
            print('finito')
        else:
            self.quiz.index += 1
            self.quiz.parameters = {'amount': 10, 'category': 18, 'difficulty': self.quiz.difficulty[self.quiz.index], 'type': 'boolean'}
            print(self.quiz.parameters)
            if self.quiz.parameters['difficulty'] == 'medium':
                self.level_up(self.quiz.get_data())
            if self.quiz.parameters['difficulty'] == 'hard':
                self.question_data_level_3 = self.quiz.get_data()

            q_text = self.quiz.next_question()


        self.canvas.itemconfig(self.question_text, text=q_text)

    def x_button(self):
        is_right = self.buttons_funk('False')
        self.give_feedback(is_right)

    def v_button(self):
        is_right = self.buttons_funk('True')
        self.give_feedback(is_right)

    def buttons_funk(self, true_false):
        q_answer = self.quiz.check_answer()
        if q_answer == true_false:
            self.score += 1
            self.score_bord.config(text=f'score:{self.score}')
            return True
        else:
            return False

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(highlightbackground='green', highlightthickness=10)
        else:
            self.canvas.config(highlightbackground='red', highlightthickness=10)
        self.window.after(1000, func=self.get_next_question)

    def level_up(self, question_data):
        question_bank = []
        for question in question_data:
            question_bank.append(
                Question(
                    question["question"],
                    question["correct_answer"]
                )
            )
        self.quiz.question_data = question_bank