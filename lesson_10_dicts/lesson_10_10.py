import json
from datetime import datetime

# базовые данные
prices = {
    "HDD_Toshiba": 2000,
    "SSD_Samsung": 8000,
    "CPU_AMD_Ryzen_7": 20000,
    "CPU_AMD_Ryzen_5": 13000
}
user_products = {}
total_price = 0

# не пустит пока не наберем 3 товара
while len(user_products) < 3:
    user_product = input('Что вы хотите приобрести: ')
    # проверка на наличие
    if user_product in prices:
        # проверка на уникальность (товара не должно быть в корзине пользователя)
        if user_product not in user_products:
            product_quantity = input("В каком количестве (шт.): ")
            # проверка на то что было введено число product_quantity
            if product_quantity.isdigit():
                # подсчет итоговой цены конкретного товара
                product_total_price = prices[user_product] * int(product_quantity)
                # наполнение словаря покупок пользователя >> 'SSD_Samsung': ['2', 16000]
                user_products[user_product] = [product_quantity, product_total_price]
                total_price += product_total_price
                print(f'Товар {user_product} в количестве {product_quantity} добавлен в корзину.')
            else:
                print(f'Ошибка ввода, количество может быть только целым числом!')
        else:
            print(f'Товар {user_product} уже есть у вас в корзине.')
    else:
        print(f'Простите, данного товара нет в ассортименте.')

# {'SSD_Samsung': ['2', 16000], 'CPU_AMD_Ryzen_7': ['3', 60000], 'CPU_AMD_Ryzen_5': ['1', 13000]}

# вывод итоговых покупок
for key, value in user_products.items():
    quantity, product_price = value
    print(f'{key} в количестве: {quantity} штук, стоимость {product_price}')
print(f'Общая стоимость: {total_price}.')

# запись данных в файл
with open(fr'user_orders_{datetime.now().strftime("%Y%m%d_%H_%M_%S")}.json', 'w', encoding='utf-8') as fp:
    json.dump(user_products, fp, ensure_ascii=False, indent=2)
