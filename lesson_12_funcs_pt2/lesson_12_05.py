def remove_from_string(string, *args):
    print(args)
    for symbol in args:
        string = string.replace(symbol, '')
    return string


def make_upper(string, *args):
    string_list = string.split()
    new_string_list = []
    for word in string_list:
        for word_to_upper in args:
            if word.startswith(word_to_upper):
                word = word.upper()
                break
        new_string_list.append(word)
    return ' '.join(new_string_list)


if __name__ == '__main__':
    print(remove_from_string('О! Смотри, можно "удалить" все знаки: препинания сразу?', '!', ',', '.', '?', ':', '"'))
    user_string = input("Введите строку: ")
    user_words = input('Введите слова для изменения регистра через пробел: ').split()
    print(make_upper(user_string, *user_words))
