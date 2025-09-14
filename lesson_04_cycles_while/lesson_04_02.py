# even_numbers = 0
# odd_numbers = 0
#
# user_number = int(input("Введите число или 0 для остановки программы: "))
#
# while user_number != 0:
#     if user_number % 2 == 0:
#         even_numbers += 1
#     else:
#         odd_numbers += 1
#     user_number = int(input("Введите число или 0 для остановки программы: "))
#
# print(f"Количество четных чисел {even_numbers}")
# print(f"Количество нечетных чисел {odd_numbers}")


# while True:
#     user_choice = input('Введите 1 - для продолжения цикла, 0 - для его остановки: ')
#     if user_choice == '0':
#         print("Цикл остановлен")
#         break
#     elif user_choice == '1':
#         print('Цикл продолжается')
#     else:
#         print('Неверный ввод')


# user_input = input("Введите 1 для старта программы по алгоритму 1\n2 для старта программы по алгоритму 2\nВаш выбор: ")

# while user_input not in ['1', '2']:
#     print("Ошибка ввода!")
#     user_input = input(
#         "Введите 1 для старта программы по алгоритму 1\n2 для старта программы по алгоритму 2\nВаш выбор: ")
#
# if user_input == '1':
#     print('Выполняю программу 1')
# else:
#     print('Выполняю программу 2')
#
# user_input = input("Введите 1 для старта программы по алгоритму 1\n2 для старта программы по алгоритму 2\nВаш выбор: ")
#
# while user_input != '1' and user_input != '2':
#     print("Ошибка ввода!")
#     user_input = input(
#         "Введите 1 для старта программы по алгоритму 1\n2 для старта программы по алгоритму 2\nВаш выбор: ")
#
# if user_input == '1':
#     print('Выполняю программу 1')
# else:
#     print('Выполняю программу 2')

var1 = 1000
var2 = 50

while type(var1) is int and 0 <= var2 <= 100:
    print('Внутри цикла')
    var1 = 1000
    var2 = 101
