# pets_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
# pets_dict_keys = pets_dict.keys()
# print(pets_dict_keys)
# print(type(pets_dict_keys))
# pets_dict_keys_list = list(pets_dict_keys)
# print(pets_dict_keys_list)
# print(pets_dict_keys_list[1])
# print()
#
# pets_dict_values = pets_dict.values()
# print(pets_dict_values)
# print(type(pets_dict_values))
# pets_dict_values_list = list(pets_dict_values)
# print(pets_dict_values_list)
# print(pets_dict_values_list[1])
# print()
#
# pets_dict_items = pets_dict.items()
# print(pets_dict_items)
# print(type(pets_dict_items))
# pets_dict_items_list = list(pets_dict_items)
# print(pets_dict_items_list)
# print(pets_dict_items_list[1])
# print()
#
# print('Cat' in pets_dict)  # print('Cat' in pets_dict.keys())
# print('Кошка' in pets_dict.values())
# print(('Cat', 'Кошка') in pets_dict.items())

pets_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица', 'Snake': 'Змея'}

print('Ключи словаря: ')
for key in pets_dict:  # for key in pets_dict.keys()
    print(key, end=', ')
print('\n')

print('Значения словаря: ')
for value in pets_dict.values():
    print(value, end=', ')
print('\n')

for key, value in pets_dict.items():
    # print((key, value))
    print(f'Ключ: {key}. Значение: {value}.')
print()

# создать новый словарь с фильтрацией
new_pets_dict = {}
for key, value in pets_dict.items():
    if value in ['Птица', 'Змея']:
        continue
    new_pets_dict[key] = value
print(new_pets_dict)
print()

keys_list = []
values_list = []
for key, value in pets_dict.items():
    keys_list.append(key)
    values_list.append(value)
print(keys_list)
print(values_list)
print()

animal = ('cat', 'кошка')
word, translate = animal
print(word)
print(translate)

animal_dict = dict([('cat', 'кошка'), ('dog', 'собака')])
print(animal_dict)
print(animal_dict.items())