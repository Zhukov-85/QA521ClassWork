# # cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# # literature_category_list = ["Поэма", "Роман", "Новелла", "Пьеса", "Проза"]
# #
# # for category in cinema_category_list:
# #     print(category)
# # print()
# #
# # for item in literature_category_list:
# #     print(item)
# # print()
# #
# # if len(cinema_category_list) == len(literature_category_list):
# #     for index in range(len(cinema_category_list)):
# #         print(f'Кино: {cinema_category_list[index]}. Литература: {literature_category_list[index]}')
# # else:
# #     print(f'Ошибка! Списки должны быть равной длины.')
#
# # append - добавление ОДНОГО элемента в список, с конца.
# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# cinema_category_list.append('Horror')
# print(cinema_category_list)
#
# # + - создание нового списка из нескольких списков
# new_categories = ['Detective', 'Mystery']
# all_categories = cinema_category_list + new_categories
# print(all_categories)
#
# # extend - добавление нескольких элементов в список из других коллекция (кортеж, множество)
# new_categories = ['Romance', 'Peplum']
# cinema_category_list.extend(new_categories)
# print(cinema_category_list)
#
# # insert - добавляет элемент по индексу если индекс за пределами списка,
# # попадет либо в конец (для положительных индексов, либо в начало для отрицательных)
# cinema_category_list.insert(3, 'Animation')
# print(cinema_category_list)
#
# # remove - удаление элемента из списка
# category_to_remove = "Horror"
# if category_to_remove in cinema_category_list:
#     cinema_category_list.remove(category_to_remove)
# else:
#     print(f'Жанра нет в списке')
# print(cinema_category_list)
#
# # pop - с параметром >> удаление по индексу / без параметра >> удаление последнего
# popped_category = cinema_category_list.pop(3)
# print(popped_category)
# popped_category_last = cinema_category_list.pop()
# print(popped_category_last)
# print(cinema_category_list)
#
# # если список будет меняться в цикле, цикл запускать по копии списка
# for item in cinema_category_list[:]:
#     if item in ['Comedy', 'Action']:
#         cinema_category_list.remove(item)
#
# print(cinema_category_list)
#
# # clear - очистка списка.
# cinema_category_list.clear()
# print(cinema_category_list)


cinema_category_list = ["Action", "Drama", "Comedy", "Fantasy", "Scy-Fy", "Comedy", "Action"]
category_to_find = 'Fantasy'
if category_to_find in cinema_category_list:
    item_idx = cinema_category_list.index(category_to_find)
    print(item_idx)

print(cinema_category_list.count('Comedy'))

print(cinema_category_list)
cinema_category_list.sort()
print(cinema_category_list)
cinema_category_list.sort(reverse=True)
print(cinema_category_list)

cinema_category_list = ["Action", "Drama", "Comedy", "Fantasy", "Scy-Fy", "Comedy", "Action"]
# reverse - отзеркалить список
cinema_category_list.reverse()
print(cinema_category_list)

print("Action" in cinema_category_list)
print("Horror" in cinema_category_list)
print("Action" not in cinema_category_list)
print("Horror" not in cinema_category_list)
