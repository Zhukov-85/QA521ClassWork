iter_counter = 5

while iter_counter != 0:
    print(f'Внутри цикла: {iter_counter}')
    iter_counter -= 1

print(f'Вне цикла: {iter_counter}')
print()

iter_counter = 0

while iter_counter != 5:
    print(f'Внутри цикла: {iter_counter}')
    iter_counter += 1

print(f'Вне цикла: {iter_counter}')
print('Вне цикла:', iter_counter)
# print('Вне цикла: {}'.format(iter_counter))
