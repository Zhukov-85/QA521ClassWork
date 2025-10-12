# def get_file_data(filepath):
#     try:
#         file = open(filepath, 'rt', encoding='utf-8')  # encoding=encoding ОБЯЗАТЕЛЬНО
#         content = file.read()
#         if file:
#             file.close()
#         return content
#     except FileNotFoundError:
#         print(f'Файл не найден в указанном расположении:\n{filepath}')
#         return False
#     except Exception as Ex:
#         print(type(Ex).__name__)
#         return False

def get_file_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f'Файл не найден в указанном расположении:\n{filepath}')
        return False
    except Exception as Ex:
        print(type(Ex).__name__)
        return False


def get_file_lines(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines_list = []
            for line in file:
                lines_list.append(line.rstrip())
        return lines_list
    except FileNotFoundError:
        print(f'Файл не найден в указанном расположении:\n{filepath}')
        return False
    except Exception as Ex:
        print(type(Ex).__name__)
        return False


if __name__ == '__main__':
    my_filepath = r'example_files\managers_data.txt'
    print(get_file_data(my_filepath))
    print(get_file_lines(my_filepath))
