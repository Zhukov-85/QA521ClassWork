num = 10
print(type(num), num)
num = float(num)
print(type(num), num)
num = str(num)
print(type(num), num)  # '10.0'
print()

print('Введите 1 - да, 2 - нет: ')

"""
ПЛОХО НЕ ДЕЛАТЬ ТАК!
"""
# user_choice = int(input())
#
# if user_choice == 1:
#     print('Да')
# elif user_choice == 2:
#     print('Нет')
# else:
#     print('Некорректный ввод')

"""
ВЕРНЫЙ ПОДХОД
"""
user_choice = input()

if user_choice == "1":
    print('Да')
elif user_choice == "2":
    print('Нет')
else:
    print('Некорректный ввод')


