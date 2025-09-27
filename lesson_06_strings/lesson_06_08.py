# # .count() - подсчет количества вхождений указанной подстроки в строке
# my_str = 'Hello World! Hello Python!'
# o_count = my_str.count('o')
# print(o_count)
# o_count1 = my_str.count('o', 10, 20)
# print(o_count1)
# hello_count = my_str.count('Hello')
# print(hello_count)

# # .find() поиск индекса 1го вхождения элемента в строке
# # если символ не найден вернет -1
# my_str = 'Hello World! Hello Python!'
# element_index = my_str.find('o')
# print(element_index)
# element_index1 = my_str.find('o', 5, 10)
# print(element_index1)
# start_index = my_str.find("World!")
# print(start_index)
# print()

# # .rfind() поиск индекса 1го вхождения элемента в строке c конца строки
# # если символ не найден вернет -1
# my_str = 'Hello World! Hello Python!'
# element_index = my_str.rfind('o')
# print(element_index)
# element_index1 = my_str.rfind('o', 10, 20)
# print(element_index1)
# start_rindex = my_str.rfind("Hello")
# print(start_rindex)

# # .index() поиск индекса 1го вхождения элемента в строке
# # если элемент не найден получим >> ValueError: substring not found
# my_str = 'Hello World! Hello Python!'
# element_index = my_str.index('o')
# print(element_index)
# element_index1 = my_str.index('o', 5, 10)
# print(element_index1)
# start_index = my_str.index("World")
# print(start_index)
# print()
#
# # .rindex() поиск индекса 1го вхождения элемента в строке c конца строки
# # если элемент не найден получим >> ValueError: substring not found
# my_str = 'Hello World! Hello Python!'
# element_index = my_str.rindex('o')
# print(element_index)
# element_index1 = my_str.rindex('o', 10, 20)
# print(element_index1)
# start_rindex = my_str.rindex("Hello")
# print(start_rindex)
# print()

# .startswith() - проверка с чего начинается строка
# .endswith() - проверка окончания строки
my_str = 'Hello World! Hello Python!'
print(my_str.startswith('H'))
print(my_str.startswith('Hello'))
print(my_str.endswith('!'))
print(my_str.endswith('Python!'))
print()

print(my_str.startswith('World', 6))
print(my_str.startswith('World', 6, 11))
print(my_str.endswith('Hello', 13, 18))
print(my_str.endswith('World', 6, 11))


