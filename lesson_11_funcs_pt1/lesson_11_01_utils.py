import random

def display_random_gift():
    gifts = ["барбариски", "мячик", "машинка", "конструктор"]
    random_gift = random.sample(gifts, 1)[0]
    print(random_gift)


if __name__ == '__main__':
    # print(display_random_gift.__module__)
    while True:
        user_input = input(
            "Введите stop/стоп для остановки или enter для получения случайного подарка: ").strip().lower()
        if user_input in ['stop', 'стоп']:
            break
        display_random_gift()



