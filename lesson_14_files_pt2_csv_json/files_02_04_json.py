import json


def get_data_from_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            python_data = json.load(file)
    except FileNotFoundError:
        print(f'Файл не найден!')
        return False
    except json.JSONDecodeError:
        print(f'Ошибка декодирования файла')
        return None

    return python_data


def get_data_from_json_string(data):
    try:
        python_data = json.loads(data)
    except json.JSONDecodeError:
        print(f'Ошибка декодирования строки')
        return False
    return python_data


if __name__ == '__main__':
    my_filename = r'files\data.json'
    my_data = get_data_from_json(my_filename)
    print(my_data, type(my_data))

    json_string = '{"0": "Нулевой", "1": true, "2": false, "3": null, "4": ["data1", "data2"], "5": {"key1": "value1"}}'
    my_python_data = get_data_from_json_string(json_string)
    print(my_python_data, type(my_python_data))
