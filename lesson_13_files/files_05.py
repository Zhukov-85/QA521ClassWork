import datetime


def get_question_data(filename) -> list[str]:
    with open(filename, 'r', encoding='utf-8') as file:
        questions = file.readlines()
    return questions


def write_user_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(f'{line}\n')
    return True


if __name__ == '__main__':
    # user_questions = [
    #     "Введите ваше имя: ",
    #     "Какой иностранный язык вы изучаете: ",
    #     "Как долго: ",
    #     "Где: "
    # ]
    questions_source = input(f'Введите имя файла с вопросами: ')
    questions_file = fr'example_files\{questions_source}.txt'
    user_questions = []
    user_answers = []
    try:
        user_questions = get_question_data(questions_file)
    except Exception as ex:
        print(type(ex).__name__)

    if user_questions:
        for question in user_questions:
            user_answer = input(f'{question.rstrip()} ')
            user_answers.append(user_answer)
        now = datetime.datetime.now()
        now_formatted = now.strftime('%Y_%m_%d_%H_%M_%S')
        user_filename = fr'example_files\{now_formatted}_{user_answers[0]}_answers.txt'
        try:
            write_user_data(user_filename, user_answers)
        except Exception as ex:
            print(type(ex).__name__)
    else:
        print(f'Вопросы не были получены')
