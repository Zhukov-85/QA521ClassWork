pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
print(pets_dict['cat'])

pets_dict['die Katze'] = pets_dict['cat']
print(pets_dict)
del pets_dict['cat']
print(pets_dict)

# popped_data = pets_dict.pop('dog')
# print(popped_data)
# pets_dict['der Hund'] = popped_data
# print(pets_dict)
pets_dict['der Hund'] = pets_dict.pop('dog')  # pets_dict['der Hund'] = Собака
print(pets_dict)

