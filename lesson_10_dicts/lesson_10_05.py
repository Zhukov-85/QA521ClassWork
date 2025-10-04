# pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
#
# animal = input('Введите слово для перевода: ')
# if animal in pets_dict:
#     print(pets_dict[animal])
# else:
#     print("Не знаю таких слов.")
#
#
# try:
#     print(pets_dict[animal])
# except KeyError as ke:
#     print(type(ke).__name__, ke)
#     print(f'{animal} нет в словаре')
# finally:
#     print('Программа завершила работу!')
# print()

pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
translation1 = pets_dict.get('cat', 'нет в словаре')
print(translation1)
translation2 = pets_dict.get('snake', 'нет в словаре')
print(translation2)
print(pets_dict)
print()

translation3 = pets_dict.setdefault('owl')
print(translation3)
print(pets_dict)
# pets_dict['owl'] = 'Сова'
print()

translation4 = pets_dict.setdefault('snake', 'Змея') # {'cat': 'Кошка', 'dog': 'Собака', 'owl': None, 'snake': 'Змея'}
print(translation4)
print(pets_dict)
