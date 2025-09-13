# full_day = 24 * 60 * 60
#
# user_seconds = int(input("Введите время в секундах, прошедшее с начала дня: "))
#
# if user_seconds < full_day:
#     user_choice = input("Введите как отобразить оставшееся время: 1 - часы, 2 - минуты, 3 - секунды: ")
#     if user_choice == '1':
#         time_remaining = 24 - user_seconds / 3600
#         print(f"Осталось часов: {round(time_remaining, 2)}")
#     elif user_choice == '2':
#         time_remaining = 24 * 60 - user_seconds / 60
#         print(f"Осталось минут: {round(time_remaining, 2)}")
#     elif user_choice == '3':
#         time_remaining = full_day - user_seconds
#     else:
#         print('Ошибка ввода! Введите 1, 2 или 3.')
# else:
#     print(f"Ошибка в сутках всего: {full_day} секунд.")


# user_month = input("Введите номер месяца: ")
#
# if user_month in ['1', '2', '12']:
#     print('winter')
# elif user_month in ['3', '4', '5']:
#     print('spring')
# elif user_month in ['6', '7', '8']:
#     print('summer')
# elif user_month in ['9', '10', '11']:
#     print('autumn')
# else:
#     print('Ошибка в году всего 12 месяцев!')

user_num = input('Введите целое шестизначное число: ')
if len(user_num) != 6:
    print('Вы ввели не шестизначное число!')
elif not user_num.isdigit():
    print('Вы ввели не целое число!')
else:
    user_num = int(user_num)
    digit01 = user_num // 100000
    digit02 = user_num % 100000 // 10000
    digit03 = user_num % 100000 % 10000 // 1000
    digit04 = user_num % 100000 % 10000 % 1000 // 100
    digit05 = user_num % 100000 % 10000 % 1000 % 100 // 10
    digit06 = user_num % 100000 % 10000 % 1000 % 100 % 10
    if digit01 + digit02 + digit03 == digit04 + digit05 + digit06:
        print('Счастливое число!')
    else:
        print('Несчастливое число!')
print()

user_num = input('Введите целое шестизначное число: ')
if len(user_num) != 6:
    print('Вы ввели не шестизначное число!')
elif not user_num.isdigit():
    print('Вы ввели не целое число!')
else:
    user_num = int(user_num)
    digit01 = user_num // 100000
    digit02 = user_num % 100000 // 10000
    digit03 = user_num % 100000 % 10000 // 1000
    digit04 = user_num % 100000 % 10000 % 1000 // 100
    digit05 = user_num % 100000 % 10000 % 1000 % 100 // 10
    digit06 = user_num % 100000 % 10000 % 1000 % 100 % 10
    print(str(digit06) + str(digit05) + str(digit03) + str(digit04) + str(digit02) + str(digit01))
print()

user_num = input('Введите целое шестизначное число: ')
if len(user_num) != 6:
    print('Вы ввели не шестизначное число!')
elif not user_num.isdigit():
    print('Вы ввели не целое число!')
else:
    print(user_num[5] + user_num[4] + user_num[2] + user_num[3] + user_num[1] + user_num[0])
