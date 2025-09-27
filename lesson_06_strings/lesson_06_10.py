my_str_alnum = 'Helloworld12345'
print(my_str_alnum.isalnum())

my_str_alnum = 'Helloword'
print(my_str_alnum.isalnum())

my_str_alnum = '12345'
print(my_str_alnum.isalnum())

my_str_alnum = 'Helloworld12345$()'
print(my_str_alnum.isalnum())
print()

my_str_alpha = "HelloWorld"
print(my_str_alpha.isalpha())
print()

my_str_digits = '12345678946'
print(my_str_digits.isdigit())
print()

my_space_string = ' \n\t\r'
print(my_space_string.isspace())

user_name = input('Введите ваше имя: ')
if user_name.isalpha():
    print(f'Имя: {user_name} принято!')
else:
    print(f'Ошибка: имя может состоять только из букв.')
