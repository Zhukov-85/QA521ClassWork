my_str = 'Hello World! Hello Python!'
print(len(my_str))
my_str_len = len(my_str)
print(my_str[my_str_len - 1])
print(type(my_str_len))

my_str = 'Hello World! Hello Python!'
if len(my_str) > 10:
    print('Ошибка строка должна состоять не более чем из 10 символов!')
else:
    print("Все ок!")

