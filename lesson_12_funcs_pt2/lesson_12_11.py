def calculate_way(v_l, t_l, v_d, t_d):
    way_l = v_l * t_l
    way_d = v_d * t_d
    return way_l, way_d


if __name__ == '__main__':
    data_list = [60, 2]
    data_dict = {'v_d': 60, 't_d': 3}
    result_l, result_d = calculate_way(*data_list, **data_dict)
    print(f'Распаковка списка и словаря:\nсписок - {result_l}\nсловарь - {result_d}')
