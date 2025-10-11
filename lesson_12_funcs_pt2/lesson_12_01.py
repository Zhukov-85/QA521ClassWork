def get_total_check(prices: list[int], tip=0):
    temp_total = sum(prices)
    total = temp_total * (100 + tip) / 100
    return total


if __name__ == '__main__':
    sum_list = [1000, 3000, 5000]
    total_0 = get_total_check(sum_list)
    print(total_0)

    total_10 = get_total_check(sum_list, 10)
    print(total_10)

    total_20 = get_total_check(sum_list, tip=20)
    print(total_20)