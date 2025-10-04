my_dict = {}
print(my_dict)
print(type(my_dict))

my_dict1 = dict()
print(my_dict1)
print()

my_dict2 = {'Петр': 201, 'Мария': 201}
print(my_dict2)

# my_dict2 = {'Петр': 201, 'Петр': 202}
# print(my_dict2)

my_dict3 = {('mts', 'mts'): 50, 3: 'integer', 2.5: 'float', 'employees_list': ['Петр', 'Мария']}
print(my_dict3[('mts', 'mts')])
print(my_dict3['employees_list'][1])
print()

my_dict4 = dict(Петр='Имя', Python='Язык программирования')
print(my_dict4)

my_dict5 = dict((('emp_list', ['Петр', 'Мария']), (2.5, 'float')))
print(my_dict5)

explanations = {True: 'Да все верно', False: 'Это неверно!'}
print(explanations[3 > 2])  # True
print(explanations[3 < 2])  # False
