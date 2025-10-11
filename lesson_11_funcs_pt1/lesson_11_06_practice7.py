def is_happy_number(number: str) -> bool:
    if len(number) != 6:
        return False
    elif not number.isdigit():
        return False

    num1 = int(number[0]) + int(number[1]) + int(number[2])
    num2 = int(number[3]) + int(number[4]) + int(number[5])
    return num1 == num2
    # if num1 == num2:
    #     return True
    # else:
    #     return False


def is_happy_number1(number: str) -> bool:
    if len(number) != 6:
        return False
    elif not number.isdigit():
        return False
    else:
        num1 = int(number[0]) + int(number[1]) + int(number[2])
        num2 = int(number[3]) + int(number[4]) + int(number[5])
        return num1 == num2


my_number1 = input('Введите шестизначное число 1: ')
my_number2 = input('Введите шестизначное число 2: ')
my_number3 = input('Введите шестизначное число 3: ')
my_numbers = [my_number1, my_number2, my_number3]
for my_number in my_numbers:
    print(is_happy_number(my_number))
