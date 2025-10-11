class DegreeErrorException(Exception):
    def __init__(self, *args, **kwargs):
        pass


def calculate_extent(num, extent):
    try:
        if not 0 <= extent <= 7:
            raise DegreeErrorException('Степень должна быть в диапазоне от 0 до 7 включительно')
    except DegreeErrorException as DEex:
        print(DEex)
        return False
    except Exception as ex:
        print(type(ex).__name__, "Что-то пошло не так")
        return False
    else:
        return f'Число {num} в степени {extent} равно: {num ** extent}'


if __name__ == '__main__':
    try:
        user_num = float(input('Введите число: '))
        user_extent = int(input('Введите степень от 0 до 7: '))
    except ValueError as ve:
        print(type(ve).__name__, "Ошибка ввода числа или степени (неверный тип данных)")
    else:
        answer = calculate_extent(user_num, user_extent)
        print(answer)
