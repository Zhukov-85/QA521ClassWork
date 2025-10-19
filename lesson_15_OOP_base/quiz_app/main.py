from Classes.Classes import QuizMaker, get_questions_from_file

if __name__ == '__main__':
    questions = get_questions_from_file(r'Classes/questions.json')
    score = 0
    english_quiz = QuizMaker(questions)
    questions_obj = english_quiz.make_quiz()

    for question in questions_obj:
        print(question.question)
        answer = input("Введите ваш ответ: ").strip().lower()
        if question.is_correct(answer):
            print(f'Ответ верный!')
            score += question.points
        else:
            print(f'Ответ неверный, верный ответ: {question.answer}')

    print(f'Ваш результат: {score}')
