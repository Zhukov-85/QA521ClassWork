def print_number_of_str_elements():
    global str_counter
    elements = ['Новелла', 1, 'Роман', 2, "Пьеса"]
    for element in elements:
        if type(element) is str:
            str_counter += 1

    print(f'Количество строк в списке: {str_counter}')


if __name__ == '__main__':
    str_counter = 0
    print(f'Значение переменной str_counter: {str_counter}')
    print_number_of_str_elements()
    print(f'Значение переменной str_counter: {str_counter}')
    print_number_of_str_elements()
    print(f'Значение переменной str_counter: {str_counter}')
