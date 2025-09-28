evens_list = [i for i in range(21) if i % 2 == 0]
print(evens_list)

evens_list_simple = []
for i in range(21):
    if i % 2 == 0:
        evens_list_simple.append(i)
print(evens_list_simple)
print()

customers = ['Bob', 'Joe', 'Anna', 'Bob', 'Nick']
customers_filtered = [customer for customer in customers if customer != "Bob" and customer != 'Nick']
print(customers_filtered)

customers = ['Bob', 'Joe', 'Anna', 'Bob', 'Nick']
customers_filtered_simple = []
for customer in customers:
    if customer != "Bob" and customer != "Nick":
        customers_filtered_simple.append(customer)
print(customers_filtered_simple)
print()

product_list = [x * y for x in range(1, 4) for y in range(1, 5)]
print(product_list)

product_list_list_simple = []
for x in range(1, 4):
    for y in range(1, 5):
        product_list_list_simple.append(x * y)
print(product_list_list_simple)
print()

my_matrix = [[x * y for x in range(1, 4)] for y in range(1, 5)]
print(my_matrix)

matrix_simple = []
for y in range(1, 5):
    nums_list = []
    for x in range(1, 4):
        nums_list.append(x * y)
    matrix_simple.append(nums_list)

print(matrix_simple)
