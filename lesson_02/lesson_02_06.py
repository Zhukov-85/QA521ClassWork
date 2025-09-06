"""
Арифметические операторы
"""

# print(3 + 5)
# print("3" + "5")
# print("am" + "fm")
# print(5 - 3)
# print(3 * 5)
# print('fm' * 3)
# print(3 ** 3)
# print(6 / 3)
# print(11 / 3)
# print(11 // 3)
# print(11 % 3)
# print(3 % 5)
#
# num = int(input('Введите число: '))
# if num % 2 == 0:
#     print('even (четное)')
# else:
#     print('odd (нечетное)')

num_4_digits = 1234
digit_1 = num_4_digits // 1000
print(digit_1)
digit_2 = num_4_digits % 1000 // 100
print(digit_2)
digit_3 = num_4_digits % 1000 % 100 // 10
print(digit_3)
digit_4 = num_4_digits % 1000 % 100 % 10
print(digit_4)
print(digit_1 + digit_2 + digit_3 + digit_4)
