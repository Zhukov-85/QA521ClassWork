def get_managers_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data_list = []
            for manager_data in file:
                data = manager_data.rstrip().split(":")
                data_list.append(data)
    except Exception as Ex:
        print(type(Ex).__name__)
        return False
    return data_list


def write_managers_data(filepath, data_matrix, separator):
    with open(filepath, 'w', encoding='utf-8') as file:
        for man, comp, head_comp in data_matrix:
            file.write(f'{manager}{separator}{company}{separator}{head_comp}\n')
    return True


if __name__ == '__main__':
    managers_data_file = r'example_files\own_data.txt'
    managers_matrix = get_managers_data(managers_data_file)
    # print(managers_matrix)
    # [
    # ['Тодд Говард', 'Bethesda', 'Microsoft'],
    # ['Джон Кармак', 'ID Software', 'Microsoft'],
    # ['Лиза Су', 'AMD', 'AMD']
    # ]
    for manager, company, head_company in managers_matrix:
        print(f'{manager} работает в компании {company}, которая принадлежит {head_company}.')

    filename = input('Введите имя файла: ')
    my_separator = input('Введите желаемый разделитель: ')
    try:
        write_managers_data(fr'example_files\{filename}.txt', managers_matrix, my_separator)
    except Exception as Ex:
        print(type(Ex).__name__)






