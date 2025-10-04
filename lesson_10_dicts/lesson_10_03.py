# pets_dict = {'cat': 'Котейка'}
# print(pets_dict)
# print(id(pets_dict))
# pets_dict['dog'] = 'Собачка'
# print(pets_dict)  # {'cat': 'Котейка', 'dog': 'Собачка'}
# print()
#
# pets_dict['cat'] = 'Кошка'
# pets_dict['dog'] = 'Собака'
# print(pets_dict)
# print(id(pets_dict))
# print()
# # my_pets = ['cat', 'dog']
# # my_pets[1] = 'собака'
# # print(my_pets)
#
# del pets_dict['cat']
# print(pets_dict)
# # print(pets_dict['cat'])

pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
shop_dict = {'parrot': 'Попугай', 'snake': 'Змея', 'cat': 'Кот'}
pets_dict.update(shop_dict)
print(pets_dict)
