# import requests
# from quiz_brain import QuizBrain
#
#
# class Data:
#
#     def __init__(self, quiz_brain: QuizBrain):
#         self.still_has_question = quiz_brain.still_has_questions()
#         self.index = 0
#         self.level = 1
#         self.levels_pest = []
#         self.difficulty = ['easy', 'medium', 'hard']
#         self.parameters = {'amount': 10, 'category': 18, 'difficulty': self.difficulty[self.index], 'type': 'boolean'}
#         self.question_data = self.get_data()
#         #self.next_level()
#
#     def get_data(self):
#         response = requests.get(url='https://opentdb.com/api.php', params=self.parameters)
#         response.raise_for_status()
#         question_data = response.json()
#         question_data = question_data['results']
#         print(self.difficulty[self.index])
#         return question_data
#
#     def get_next_level_data(self):
#         self.level += 1
#         self.index += 1
#         self.get_data()
#         print(self.index)
#         print(self.difficulty[self.index])



