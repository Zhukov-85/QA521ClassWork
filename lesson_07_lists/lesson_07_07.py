# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# new_cinema_category_list = cinema_category_list
#
# print(cinema_category_list)
# print(new_cinema_category_list)
#
# new_cinema_category_list.append('Horror')
# print(new_cinema_category_list)
# print(cinema_category_list)
#
# print(new_cinema_category_list is cinema_category_list)

# оптимальный метод
cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
new_cinema_category_list = cinema_category_list[:]
new_cinema_category_list.append('Horror')
print(new_cinema_category_list)
print(cinema_category_list)
print(new_cinema_category_list is cinema_category_list)
print()

# тоже оптимальный метод
cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
new_cinema_category_list = list(cinema_category_list)
new_cinema_category_list.append('Horror')
print(new_cinema_category_list)
print(cinema_category_list)
print(new_cinema_category_list is cinema_category_list)
print()

# тоже работает, но осторожно
cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
new_cinema_category_list = cinema_category_list.copy()
new_cinema_category_list.append('Horror')
print(new_cinema_category_list)
print(cinema_category_list)
print(new_cinema_category_list is cinema_category_list)