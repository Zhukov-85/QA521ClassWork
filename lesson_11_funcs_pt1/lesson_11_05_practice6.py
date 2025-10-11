def is_prime(number):
    """
    Оптимизированная проверка простого числа
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:  # Проверяем чётность
        return False

    # Проверяем только нечётные делители
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True


if __name__ == '__main__':
    num_input = int(input("Введите число: "))
    if is_prime(num_input):  # True/False
        print(f'Да это простое число.')
    else:
        print(f'Нет, число не является простым.')
