time = int(input("Введите время в часах: ")) % 24
luggage = False
ticket = False
money = True

print(money or ticket and not luggage and time > 6)
print((money or ticket) and not luggage and time > 6)
        # True         # True  # True   # True/False
