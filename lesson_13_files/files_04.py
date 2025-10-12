def write_data_to_file(filename, data):
    file = open(filename, 'w', encoding='utf-8')
    file.write(f'{data}\n')
    file.close()
    return True


def append_data_to_file(filename, data):
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{data}\n')
    file.close()
    return True


if __name__ == '__main__':
    my_data = """Привет, как дела?
Спасибо, все хорошо."""
    write_data_to_file('example_files/greeting.txt', my_data)
    append_data_to_file('example_files/greeting.txt', my_data)
