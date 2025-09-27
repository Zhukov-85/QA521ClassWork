# # .lower() >> вся строка приводится к нижнему регистру
# correct_answer = 'медведь'
# user_answer = input(
#     f'Назовите животное, бывает бурый, черный, белый, бамбуковый. Начинается на букву: {correct_answer[0]}.\n').lower()
#
# if user_answer == correct_answer:
#     print(f'Ваш ответ: {user_answer}. Это верный ответ:)')
# else:
#     print(f'Ваш ответ: {user_answer}. Это неверно, верный ответ: {correct_answer}')
#
# # .upper() >> вся строка приводится к нижнему регистру
# correct_answer = 'МЕДВЕДЬ'
# user_answer = input(
#     f'Назовите животное, бывает бурый, черный, белый, бамбуковый. Начинается на букву: {correct_answer[0]}.\n').upper()
#
# if user_answer == correct_answer:
#     print(f'Ваш ответ: {user_answer}. Это верный ответ:)')
# else:
#     print(f'Ваш ответ: {user_answer}. Это неверно, верный ответ: {correct_answer}')

# # .capitalize() - 1й символ строки переходит в верхний регистр, остальные в нижний
# user_name = input('Введите ваше имя: ').capitalize()
# user_surname = input('Введите вашу фамилию: ').capitalize()
# print(user_name)
# print(user_surname)
#
# # .title() - 1й символ каждого нового слова в строке переходи в верхний регистр, остальные в нижний
# user_fullname = input('Введите ваше имя и фамилию: ').title()
# print(user_fullname)

# .swapcase() - замена регистра строки на противоположный
my_string = 'hello WORLD!*$#12345'
swapped_string = my_string.swapcase()
print(swapped_string)
