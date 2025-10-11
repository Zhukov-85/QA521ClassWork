def print_list_data(some_list):
    for element in some_list:
        print(element)
    some_list.append('Триллер')
    print(some_list)


if __name__ == '__main__':
    my_list = ['Боевик', 'Комедия', 'Драма']
    print_list_data(my_list[:])
    print(my_list)
