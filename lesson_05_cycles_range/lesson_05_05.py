num = int(input("Введите целое число: "))
start = int(input("Введите с какой степени возводить: "))
end = int(input("Введите до какой степени возводить (включительно): "))

for exp in range(start, end + 1):
    result = num ** exp
    print(f'Число {num} в степени {exp}, равно: {result}')

