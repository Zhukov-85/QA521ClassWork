start = 3
finish = 7

for i in range(start, finish):
    print(f"Внутри цикла: i = {i}")
print(f'Вне цикла')
print()

for i in range(start, finish + 1):
    print(f"Внутри цикла: i = {i}")
print(f'Вне цикла')
print()

for i in range(start + 1, finish):
    print(f"Внутри цикла: i = {i}")
print(f'Вне цикла')
