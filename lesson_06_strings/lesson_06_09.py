# .replace() - меняет найденную подстроку на новую

my_str = 'Hello world! Hello python! Hello Guido!'
replaced_string = my_str.replace('Hello', 'Hi')
print(replaced_string)

replaced_string1 = my_str.replace('Hello', 'Hi', count=2)
print(replaced_string1)

replaced_string2 = my_str.replace('Hello', 'Hi').replace('world', 'Earth')
print(replaced_string2)

my_str = 'Hello world###! Hello python&&&! Hello Guido!'
replaced_string3 = my_str.replace('#', '@').replace('&', '#').replace('@', '&')
print(replaced_string3)


def some_func(new_param=None):
    base_param = 'Базовый параметр для действий функции'
    if new_param:
        temp_param_val = base_param
        base_param = new_param
        print(f'Параметр был изменен: {temp_param_val} >> {base_param}')
    else:
        print(f"Функция работает с: {base_param}")


some_func()
some_func("Новый параметр")
