"""У вас есть список дежурств на неделю. В списке дежурств нужно заменить Дениса на Татьяну."""
import random
#
# managers = ["Алексей", "Денис", "Юля", "Руслан", "Алексей", "Денис", "Юля"]
#
# for idx in range(len(managers)):
#     if managers[idx] == 'Денис':
#         managers[idx] = 'Татьяна'
#
# print(managers)

"""
У вас есть список подарков список из пятерых детей (имена придумайте сами):
gift_list = ["машинка", "барбариски", "конструктор", "мяч", "плюшевый мишка"]
children_list = [.......]

При помощи библиотеки random случайным образом извлеките подарок для к каждого ребенка так чтобы для каждого он был разный, какой из методов библиотеки использовать вы должны решить самостоятельно. Ожидаемый результат:

Коля получил: машинка
Петя получил: конструктор
....
....
....
"""

base_gifts = ["машинка", "барбариски", "конструктор", "мяч", "плюшевый мишка"]
base_children = ["Коля", 'Петя', 'Ваня', 'Юля', 'Маша']

gift_list = base_gifts[:]
children_list = base_children[:]

children_gifts = []
if len(gift_list) == len(children_list):
    for i in range(len(gift_list)):
        child = random.choice(children_list)
        gift = random.choice(gift_list)
        children_gifts.append([child, gift])
        children_list.remove(child)
        gift_list.remove(gift)

for child, gift in children_gifts:
    print(f'{child} получил: {gift}.')
