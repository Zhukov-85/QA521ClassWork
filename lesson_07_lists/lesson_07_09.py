import random
import string

# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action", "Horror", "Detective"]
# print(cinema_category_list)
# random.shuffle(cinema_category_list)
# print(cinema_category_list)
# print()
#
# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action", "Horror", "Detective"]
# category_sample = random.sample(cinema_category_list, len(cinema_category_list))
# print(cinema_category_list)
# print(category_sample)
# category_sample = random.sample(cinema_category_list, 3)
# print(category_sample)
# print()
#
# some_str = "Привет! Я Строка!"
# random_symbols = random.sample(some_str, len(some_str))
# print(random_symbols)
# result_str = ''.join(random_symbols)
# print(result_str)
# print()

cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action", "Horror", "Detective"]
random_category = random.choice(cinema_category_list)
print(random_category)
random_categories = random.choices(cinema_category_list, k=3)
print(random_categories)

for i in range(len(cinema_category_list[:])):
    random_category = random.choice(cinema_category_list)
    print(random_category)
    cinema_category_list.remove(random_category)

print(cinema_category_list)

# random_str = random.choices(string.ascii_letters, k=6)
# print(''.join(random_str))
# print()
#
# print(random.uniform(1, 5))
# print(random.random())
