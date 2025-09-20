# my_str = ''
# my_symbol = input('Введите символ: ')
# str_length = int(input("Введите длину строки: "))
#
# for i in range(str_length):
#     my_str += my_symbol
# print(my_str)

start = int(input('Введите начало диапазона: '))
end = int(input('Введите окончание диапазона: '))
if start > end:
    end, start = start, end

num_1 = int(input('Введите число в указанных границах: '))

while not start <= num_1 <= end:
    num_1 = int(input(f'Введите число в указанных границах {start} - {end}: '))

# for i in range(start, end + 1):
#     if i == num_1:
#         print(f'!{i}!')
#     else:
#         print(i)

for i in range(start, end + 1):
    if i == num_1:
        print(f'!{i}!')
        continue
    print(i)
