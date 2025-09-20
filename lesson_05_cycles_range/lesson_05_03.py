start = 0
finish = 50
step = 10

for i in range(start, finish, step):
    print(f'Внутри цикла: i = {i}')
print("Вне цикла.")
print()

for i in range(start, finish + 1, step):
    print(f'Внутри цикла: i = {i}')
print("Вне цикла.")
print()

for i in range(start + step, finish, step):
    print(f'Внутри цикла: i = {i}')
print("Вне цикла.")
