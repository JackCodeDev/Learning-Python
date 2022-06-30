from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
point = 0
quiz = QuizBrain(question_bank)
question = 0
while quiz.still_has_question():
    quiz.next_question()






