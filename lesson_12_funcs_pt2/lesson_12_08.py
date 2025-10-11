def display_my_space_address(name: str, age: int = 36, city=None, *args, **kwargs):
    print(name)
    print(age)
    if city:
        print(f'Город: {city}')
    else:
        print('Город не указан')

    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} - {value}')


if __name__ == '__main__':
    display_my_space_address('Дмитрий', 37, None, "Belarus", "Eastern Europe", planet='Earth', star='Sun')
    print()
    display_my_space_address('Дмитрий', 37, "Minsk", "Belarus", "Eastern Europe", planet='Earth', star='Sun')
    print()
    display_my_space_address('Петр')
