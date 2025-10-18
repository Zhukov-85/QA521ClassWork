import csv


def read_csv_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def get_csv_data(filename):
    csv_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)
    return csv_data


def write_data_to_csv(filepath, data):
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f'Запись прошла успешно.\nРасположение >> {filepath}')
    return filepath


if __name__ == '__main__':
    read_csv_data(r'files/personal_data.csv')
    my_csv_data = get_csv_data(r'files/personal_data.csv')
    # ['Name', 'Age', 'City']
    # ['Alice', '30', 'New York']
    # ['Bob', '25', 'Los Angeles']
    # ['Charlie', '35', 'Chicago']
    write_data_to_csv(r'files\personal_write.csv', my_csv_data)
