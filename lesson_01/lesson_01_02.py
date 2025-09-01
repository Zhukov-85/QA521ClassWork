money = int(input('Введите количество денег: '))
cost = int(input("Введите стоимость товара: "))

if money >= cost:
    print("Можно купить")
else:
    print("Нельзя купить")
