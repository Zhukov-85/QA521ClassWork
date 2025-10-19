import json


class Question:

    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points

    def is_correct(self, user_answer):
        return self.answer == user_answer


class QuizMaker:

    def __init__(self, questions: list):
        self.questions = questions
        self.questions_obj = []

    def make_quiz(self):
        for question in self.questions:
            question_items = list(question.items())[0]
            # ("My name __ Vova": ["is", 10])
            question_task = question_items[0]
            answer, points = question_items[1]
            self.questions_obj.append(Question(question_task, answer, points))
        return self.questions_obj


def get_questions_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        question_list = json.load(fp)
    return question_list
