def new_sum(*args):
    print(args)
    list_args = list(args)
    print(list_args)
    sum_ = 0
    if args:
        for num in args:
            sum_ += num
        return sum_
    else:
        return f'Нечего суммировать'


if __name__ == '__main__':
    print(new_sum(2, 4, 5, 6, 7))
    print(new_sum())
