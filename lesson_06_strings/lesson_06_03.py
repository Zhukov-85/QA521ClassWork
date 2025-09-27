# my_str = "Hello World!"
#
# print("Срезы по положительным индексам")
# string_slice_01 = my_str[0:5]
# print(string_slice_01)
#
# string_slice_02 = my_str[:5]
# print(string_slice_02)
#
# string_slice_03 = my_str[6:11]
# print(string_slice_03)
#
# string_slice_04 = my_str[6:]
# print(string_slice_04)
# print()
#
# print("Срезы по отрицательным индексам")
# string_slice_05 = my_str[-6:]
# print(string_slice_05)
#
# string_slice_06 = my_str[-6:-1]
# print(string_slice_06)
# print()
#
# print("Срезы по разным индексам, не рекомендую")
# string_slice_07 = my_str[1:-1]
# print(string_slice_07)
#
# print("Срезы по индексам, которые хранятся в переменных")
# index_1 = 2
# index_2 = 7
#
# print(my_str[index_1: index_2])


# my_str = 'Hello World! Hello Python!'
# string_step_slice_01 = my_str[::2]
# print(string_step_slice_01)
#
# string_step_slice_02 = my_str[1:15:2]
# print(string_step_slice_02)
#
# string_step_slice_03 = my_str[:20:3]
# print(string_step_slice_03)
# string_step_slice_04 = my_str[10::3]
# print(string_step_slice_04)


my_str = 'Hello World! Hello Python!'
mirror_string_01 = my_str[::-1]
print(mirror_string_01)

my_str = 'Hello World! Hello Python!'
mirror_string_02 = my_str[::-2]
print(mirror_string_02)

my_str = 'Hello World! Hello Python!'
mirror_string_03 = my_str[15:1:-1]
print(mirror_string_03)
