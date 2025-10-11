import random


def get_random_gift(gifts):
    random_gift = random.sample(gifts, 1)[0]
    return random_gift


def get_random_gifts(gifts):
    random_gifts = []
    while True:
        user_input = input("Введите stop для остановки или enter для получения случайного подарка: ").strip().lower()
        if user_input in ['stop', 'стоп']:
            break
        our_gift = get_random_gift(gifts)  # вызываем функцию получения подарка
        random_gifts.append(our_gift)
    return random_gifts


if __name__ == '__main__':
    gifts_01 = ["барбариски", "мячик", "машинка", "конструктор"]
    gifts_02 = ["приставка", "кубики", "леденцы", "сборная модель"]

    my_choice_gifts_01 = get_random_gifts(gifts_01)
    print(f'Вы вытащили подарки: {', '.join(my_choice_gifts_01)}')
    my_choice_gifts_02 = get_random_gifts(gifts_02)
    print(f'Вы вытащили подарки: {', '.join(my_choice_gifts_02)}')
