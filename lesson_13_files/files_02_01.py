def get_file_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def get_file_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines_list = []
        for line in file:
            lines_list.append(line.rstrip())
    return lines_list


if __name__ == '__main__':
    my_filepath = r'example_files\managers_data.txt'
    try:
        print(get_file_data(my_filepath))
        print(get_file_lines(my_filepath))
    except FileNotFoundError:
        print(f'Файл не найден в указанном расположении:\n{my_filepath}')
    except Exception as Ex:
        print(type(Ex).__name__)
