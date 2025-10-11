from lesson_11_01_utils import display_random_gift


def func():
    pass


if __name__ == '__main__':
    # print(display_random_gift.__module__)
    # print(func.__module__)
    while True:
        user_input = input(
            "Введите stop/стоп для остановки или enter для получения случайного подарка: ").strip().lower()
        if user_input in ['stop', 'стоп']:
            break
        display_random_gift()
