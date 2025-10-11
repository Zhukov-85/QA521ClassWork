def display_planet_space_address(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} - {value}')


if __name__ == '__main__':
    display_planet_space_address('Dmitry', 36, planet="Earth", star='Sun', galaxy='Milky Way', age=round(4.543e9))
    display_planet_space_address()

