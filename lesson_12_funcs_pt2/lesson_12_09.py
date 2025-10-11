def calculate_way(v, t):
    way = v * t
    return way


if __name__ == '__main__':
    data_list = [60, 2]
    data_tuple = (50, 3)
    print(calculate_way(*data_list))
    print(calculate_way(*data_tuple))
    print(*data_list)
    print(*data_tuple)
    vl, tl = data_list
    vt, tt = data_tuple
    print(vl, tl)
    print(vt, tt)
