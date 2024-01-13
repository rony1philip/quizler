import html
import requests

class QuizBrain:

    def __init__(self):
        self.question_number = 0
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
        print(self.difficulty[self.index])
        return self.question_data

    def still_has_questions(self):
        return self.question_number < len(self.question_data)

    def next_question(self):
        self.current_question = self.question_data[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self):
        correct_answer = self.current_question.answer
        return correct_answer
