import json


def write_data_to_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        try:
            json.dump(data, file, ensure_ascii=False, indent=4)
        except TypeError:
            print(f'Object of type set is not JSON serializable')
            return False
    print(f'Данные записаны успешно!')
    return True


def make_json_string(data):
    try:
        json_string = json.dumps(data, ensure_ascii=False, indent=4)
    except TypeError:
        print(f'Object of type set is not JSON serializable')
        return False
    return json_string


if __name__ == '__main__':
    my_filename = r'files\data.json'
    my_data = {
        0: 'Нулевой',
        1: True,
        2: False,
        3: None,
        4: ('data1', 'data2'),
        5: {'key1': 'value1'}
    }

    write_data_to_json_file(my_filename, my_data)

    my_json_string = make_json_string(my_data)
    print(my_json_string)
    print(type(my_json_string))
