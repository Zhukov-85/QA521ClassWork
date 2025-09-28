# category_list = ["Drama", "Comedy", "Fantasy", 'Action', 'Tragedy', 'Scy-fy']
# print(category_list)
# print(category_list[0])
# print(category_list[-1])
# print(category_list[:3])
# print(category_list[3:])
# print(category_list[2:5])
# print(category_list[::2])
# print(category_list[1:5:2])
# print(category_list[::-1])
# # print(category_list[10])

# category_list = ["Drama", "Comedy", "Fantasy"]
# category_list[0] = 'Action'
# category_list[1] = 'Tragedy'
# category_list[2] = 'Scy-Fy'
# print(category_list)

category_list = ["Drama", "Comedy", "Fantasy", 'Action', 'Tragedy', 'Scy-fy']
category_list_1 = ["Drama", "Daama", "Dzama", "Dlama"]
"""
[0-9A-Za-zА-Яа-я]
"""
nums_list = [3, 1, 4, 2, 11, 25, 2.5]

print(len(category_list), len(nums_list))
print(max(category_list), max(nums_list))
print(max(category_list_1))
print(min(category_list), min(nums_list))
print(sum(nums_list))
print(', '.join(category_list))

sorted_category_list = sorted(category_list)
sorted_nums_list = sorted(nums_list)
print(category_list)
print(sorted_category_list)
print(sorted_nums_list)
print()

sorted_category_list_rev = sorted(category_list, reverse=True)
sorted_nums_list_rev = sorted(nums_list, reverse=True)
print(category_list)
print(sorted_category_list_rev)
print(sorted_nums_list_rev)


example_list_nums_str = ['03', '1', '02', '11', '0100', "Apple"]
sorted_example_list_nums_str = sorted(example_list_nums_str)
print(sorted_example_list_nums_str)