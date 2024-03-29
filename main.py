from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []

quiz = QuizBrain()

question_data = quiz.question_data



for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz.question_data = question_bank

quiz_ui = QuizInterface(quiz,new_question)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
