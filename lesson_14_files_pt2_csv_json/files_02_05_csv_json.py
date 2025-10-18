import csv
import json


def get_data_from_csv(filepath):
    csv_data = []
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_data.append(row)

    return csv_data


def write_data_to_json(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        print(f'Данные записаны успешно!')
    except TypeError:
        print(f'Ошибка в данных!')
    return filename


if __name__ == '__main__':
    my_csv_data = get_data_from_csv(r'files\personal_data.csv')
    # [
    # {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    # {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'},
    # {'Name': 'Charlie', 'Age': '35', 'City': 'Chicago'}
    # ]
    write_data_to_json(r'files\personal_data.json', my_csv_data)
