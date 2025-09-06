my_item = 'item_1'
friend_item = 'item_2'

print(my_item, friend_item)
print(my_item, friend_item, sep=':')
print(my_item, friend_item, sep=' : ')
print()
print(my_item)
print(friend_item)
print()
print(my_item, end=' * ')
print(friend_item)
print(my_item, end='\n')
print(friend_item)
print()

pets_list = ['cat', 'dog', 'owl', 'parrot']

for pet in pets_list:
    print(pet, end=' : ')
