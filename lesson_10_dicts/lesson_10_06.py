fruits = {
    'яблоки': 100,
    'груши': 200,
    'персики': 400
}

fruit = input('Выберете фрукт: ')
# weight = float(input('Вес в граммах: '))

if fruit in fruits:
    weight = float(input('Вес в граммах: '))
    price = fruits[fruit] * weight / 1000
    print(f'Стоимость: {price} рублей')
else:
    print(f'{fruit} нет в ассортименте.')
