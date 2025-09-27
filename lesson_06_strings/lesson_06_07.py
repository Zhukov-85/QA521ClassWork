# # .strip() - удаления пробелов слева и справа
# # .rstrip() - удаления пробелов справа (полезно при работе с текстовыми файлами)
# # .lstrip() - удаления пробелов слева
#
# correct_answer = 'медведь'
# user_answer = input(
#     f'Назовите животное, бывает бурый, черный, белый, бамбуковый. Начинается на букву: {correct_answer[0]}.\n').strip()
#
# if user_answer == correct_answer:
#     print(f'Ваш ответ: {user_answer}. Это верный ответ:)')
# else:
#     print(f'Ваш ответ: {user_answer}. Это неверно, верный ответ: {correct_answer}')
#
# strings_list = ['   строка1\n', 'строка2\n', 'строка\n']
# for string in strings_list:
#     print(string.rstrip())


correct_answer = 'Медведь'
user_answer = input(
    f'Назовите животное, бывает бурый, черный, белый, бамбуковый. Начинается на букву: {correct_answer[0]}.\n').strip().capitalize()

if user_answer == correct_answer:
    print(f'Ваш ответ: {user_answer}. Это верный ответ:)')
else:
    print(f'Ваш ответ: {user_answer}. Это неверно, верный ответ: {correct_answer}')
