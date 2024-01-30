import html
import requests


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.question_number_t = 0
        self.score = 0
        self.current_question = None
        self.index = 0
        self.level = 1
        self.difficulty = ['easy', 'medium', 'hard']
        self.parameters = {'amount': 10, 'category': 18, 'difficulty': self.difficulty[self.index], 'type': 'boolean'}
        self.question_data = self.get_data()


    def get_data(self):
        response = requests.get(url='https://opentdb.com/api.php', params=self.parameters)
        response.raise_for_status()
        question_data = response.json()
        self.question_data = question_data['results']
        print(f'{0} {self.question_data}')
        return self.question_data

    def still_has_questions(self):
        return self.question_number < len(self.question_data)

    def next_question(self):
        self.question_num_config()
        self.current_question = self.question_data[self.question_number]
        self.question_number += 1
        self.question_number_t += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def question_num_config(self):
        if self.question_number_t == 10 or self.question_number_t == 20:
            self.question_number = 0

    def check_answer(self):
        correct_answer = self.current_question.answer
        return correct_answer
