my_string = 'Hello World!'
center_string = my_string.center(20)
print(center_string)
center_string = my_string.center(20, '*')
print(center_string)
center_string = my_string.center(3, '*')
print(center_string)
print()

my_string = 'Hello World!'
print(my_string.ljust(20))
print(my_string.ljust(20, '*'))
print(my_string.ljust(3, '*'))
print()

my_string = 'Hello World!'
print(my_string.rjust(20))
print(my_string.rjust(20, '*'))
print(my_string.rjust(3, '*'))
