def calculate_way(v, t):
    way = v * t
    return way


if __name__ == '__main__':
    data_dict = {'v': 60, 't': 3}
    print(f'Распаковка словаря: {calculate_way(**data_dict)}')
    # print(f'Распаковка словаря: {calculate_way(v=60, t=3)}')
