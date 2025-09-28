my_list = [2 ** i for i in range(10)]
print(my_list)

my_list_simple = []
for i in range(10):
    value = 2 ** i
    my_list_simple.append(value)
print(my_list_simple)
print()



square_list = [i * i for i in range(11)]
print(square_list)

square_list_simple = []
for i in range(11):
    value = i * i
    square_list_simple.append(value)
print(square_list_simple)
print()

list_from_str = [symbol + '*' for symbol in 'my_string']
print(list_from_str)
restored_string = ''.join(list_from_str)
print(restored_string)

list_from_str_simple = []
for symbol in 'my_string':
    value = symbol + '*'
    list_from_str_simple.append(value)
print(list_from_str_simple)

list_from_str_2 = [sym * 5 for sym in 'abcd']
print(list_from_str_2)

list_from_str_3 = []
for sym in 'abcd':
    list_from_str_3.append(sym * 5)
print(list_from_str_3)