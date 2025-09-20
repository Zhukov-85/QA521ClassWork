# number = 3
#
# for i in range(5):
#     if i == number:
#         break
#     print(f'i = {i}')
# print(f'Вышли из цикла.')


# number_1 = 3
# number_2 = 5
#
# for i in range(10):
#     if i == number_1:
#         continue
#     elif i == number_2:
#         continue
#     print(f'i == {i}')
# print(f'Вышли из цикла.')

# number_1 = 3
# number_2 = 5
#
# for i in range(10):
#     if i == number_1 or i == number_2:
#         continue
#     print(f'i == {i}')
# print(f'Вышли из цикла.')
# print()

# number_1 = 3
# number_2 = 5
#
# for i in range(10):
#     if i == number_1 or i == number_2:
#         pass
#     print(f'i == {i}')
# print(f'Вышли из цикла.')

number_1 = 3
for i in range(10):
    if i == number_1:
        break
    print(f'i == {i}')
else:
    print(f'Цикл закончен без прерываний')
print(f'Вышли из цикла.')
print()

number_1 = 11
for i in range(10):
    if i == number_1:
        break
    print(f'i == {i}')
else:
    print(f'Цикл закончен без прерываний')
print(f'Вышли из цикла.')
print()


animals_list = ['cat', 'dog', 'snake', 'owl', 'parrot', 'lion']
animal_to_break = 'lion'

for animal in animals_list:
    if animal == animal_to_break:
        print(f'{animal_to_break} найден в списке')
        break
    print(animal)
else:
    print(f'{animal_to_break} не найден в списке')
print("Список проверен циклом")
