even_numbers = 0
odd_numbers = 0

user_number = int(input("Введите число или 0 для остановки программы: "))

while user_number != 0:
    if user_number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
