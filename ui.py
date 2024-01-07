from tkinter import *
from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"

class QuizInterface(QuizBrain):

    def __init__(self):
        super().__init__(q_list=None)
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.window.minsize(width=500, height=615)

        self.canvas = Canvas(width=500, height=450, bg=THEME_COLOR)
        image = PhotoImage(file="C:/Users/user/PycharmProjects/quizzier-app/images/text_books.png")
        self.canvas.create_image(253,225, image=image)
        self.question = self.canvas.create_text(253,225,text=self.current_question, font=('Courier',18,'bold') )
        self.canvas.grid(column=1, row=2, columnspan=2)

        self.score_bord = Label(width=15,text=f'score:{self.score}', fg=THEME_COLOR, font=('Courier',18,'bold'))
        self.score_bord.grid(column=2, row=1)

        t_image = PhotoImage(file='images/true.png')
        self.true = Button(image=t_image, highlightthickness=0)
        self.true.place(x=115, y=470)

        f_image = PhotoImage(file='images/false.png')
        self.true = Button(image=f_image, highlightthickness=0)
        self.true.place(x=285, y=470)

        self.window.mainloop()



