from question_model import Question
from data import question_data
from quiz import QuizBrain
from ui import UiInterface

question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
ui = UiInterface(quiz)

