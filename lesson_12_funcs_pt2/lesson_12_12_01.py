class DegreeErrorException(Exception):
    def __init__(self, *args, **kwargs):
        pass


def calculate_extent(num, extent):
    try:
        num = float(num)
        extent = int(extent)
        if not 0 <= extent <= 7:
            raise DegreeErrorException("Степень должна быть в диапазоне от 0 до 7 включительно")
    except DegreeErrorException as DEEx:
        print(DEEx)
        return False
    except ValueError as ve:
        print(type(ve).__name__, "Ошибка ввода числа или степени")
        return False
    except Exception as ex:
        print(type(ex).__name__, "Что-то пошло не так!")
        return False
    else:
        return f'Число {num} в степени {extent} равно: {num ** extent}'


if __name__ == '__main__':
    user_num = input('Введите число: ')
    user_extent = input('Введите степень от 0 до 7: ')
    answer = calculate_extent(user_num, user_extent)
    print(answer)
