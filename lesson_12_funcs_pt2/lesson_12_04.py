def get_longest_word(*args):
    print(args)
    leader = ''

    if args:
        for word in args:
            if type(word) is str:
                if len(word) > len(leader):
                    leader = word
        return leader
    return 'Нет слов'


def get_longest_list(*args):
    leader = []
    for list_ in args:
        if type(list_) is list:
            if len(list_) > len(leader):
                leader = list_[:]
    return leader


if __name__ == '__main__':
    print(get_longest_word('Python', 'Java', 2, ['java'], 'programming'))
    print(get_longest_list([1, 2], ['a', 'b', 'c'], [3], 'programming'))
