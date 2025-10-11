import random


def get_random_gift():
    gifts = ["барбариски", "мячик", "машинка", "конструктор"]
    random_gift = random.sample(gifts, 1)[0]
    return random_gift


def get_random_gifts():
    random_gifts = []
    while True:
        user_input = input("Введите stop для остановки или enter для получения случайного подарка: ").strip().lower()
        if user_input in ['stop', 'стоп']:
            break
        our_gift = get_random_gift()  # вызываем функцию получения подарка
        random_gifts.append(our_gift)
    return random_gifts


def get_random_3_gifts():
    gifts = ["барбариски", "мячик", "машинка", "конструктор"]
    random_gifts = random.sample(gifts, 3)
    return random_gifts


if __name__ == '__main__':
    my_gift = get_random_gift()
    print(f'Вы получили {my_gift}')
    my_3_gifts = get_random_3_gifts()
    print(f'Вам досталось 3 подарка: {', '.join(my_3_gifts)}')
    my_choice_gifts = get_random_gifts()
    print(f'Вы вытащили подарки: {', '.join(my_choice_gifts)}')
