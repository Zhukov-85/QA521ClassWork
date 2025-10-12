def get_shopping_list(filepath):
    items_count = 0
    items_sum = 0
    row_number = 0
    with open(filepath, encoding='utf-8') as file:
        for item_data in file:
            row_number += 1
            if item_data.count(" || ") != 2:
                print(f'!!!В строке {row_number} есть ошибка {item_data.strip()}!!!')
                continue
            temp_data = item_data.strip().split(" || ")
            item, quantity, price = temp_data
            items_count += 1
            items_sum += float(quantity) * float(price)
    return items_count, items_sum


if __name__ == '__main__':
    my_shopping_list = r'example_files\shopping_list.txt'
    my_count, my_sum = get_shopping_list(my_shopping_list)
    print(f'В списке покупок {my_count} позиций, общая сумма {my_sum} рублей.')
