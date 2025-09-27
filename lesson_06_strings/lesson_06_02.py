my_str = "Hello World!"
new_string = my_str[3]
print(new_string)
print(my_str[3])

# new_string = my_str[12]
# print(new_string)

new_string = my_str[len(my_str) - 1]
print(new_string)
print()

new_string_1 = my_str[-1]
print(new_string_1)
new_string_2 = my_str[-6]
print(new_string_2)

# new_string_3 = my_str[-13]
new_string_3 = my_str[-(len(my_str))]
print(new_string_3)

answer = "Медведь"
print(f'Назовите животное, бывает бурый, черный, белый, бамбуковый. Начинается на букву: {answer[0]}')
