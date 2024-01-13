import html
import requests

class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.current_question = None
        self.index = 0
        self.level = 1
        self.levels_pest = []
        self.difficulty = ['easy', 'medium', 'hard']
        self.parameters = {'amount': 10, 'category': 18, 'difficulty': self.difficulty[self.index], 'type': 'boolean'}
        self.question_data = self.get_data()
        print(self.question_data)


    # def next_level(self):
    #     if self.quiz.level != 3 and not self.quiz.still_has_questions():
    #         self.quiz.get_next_level_data()
    #         q_text = self.quiz.next_question()
    #         self.canvas.itemconfig(self.question_text, text=q_text)

    def get_data(self):

        if self.level != 3 and not self.still_has_questions():
            self.get_next_level_data()
        else:
            response = requests.get(url='https://opentdb.com/api.php', params=self.parameters)
            response.raise_for_status()
            question_data = response.json()
            self.question_data = question_data['results']
            print(self.difficulty[self.index])
        return self.question_data

    def get_next_level_data(self):
        self.level += 1
        self.index += 1
        ##self.parameters['difficulty'] = self.difficulty[self.index]
        self.question_data = self.get_data()['results']
        print(self.question_data)


    def still_has_questions(self):
        return self.question_number < len(self.question_data)

    def next_question(self):
        self.current_question = self.question_data[self.question_number]
        self.question_number += 1
        if self.question_number > 10:
            self.get_next_level_data()
            self.question_number = 0
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self):
        correct_answer = self.current_question.answer
        return correct_answer
        # if user_answer.lower() == correct_answer.lower():
        #     self.score += 1
        #     print("You got it right!")
        # else:
        #     print("That's wrong.")

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
