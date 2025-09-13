# car_speed = 100
# if car_speed > 50:
#     print('Машина движется быстрее 50 км/ч')
# print()
#
# car_speed = 100
# motorcycle_speed = 100
# if car_speed > motorcycle_speed:
#     print(f'Машина движется быстрее мотоцикла.')
# elif car_speed < motorcycle_speed:
#     print('Мотоцикл движется быстрее машины.')
# else:
#     print('Скорости равны')


# car_speed = 150
# motorcycle_speed = 120
#
# if car_speed > motorcycle_speed:
#     print(f'Машина движется быстрее мотоцикла.')
#     motorcycle_speed += 50
#
# if car_speed < motorcycle_speed:
#     print('Мотоцикл движется быстрее машины.')
# else:
#     print('Скорости равны')
# print()

car_speed = 150
motorcycle_speed = 120

if car_speed > motorcycle_speed:
    print(f'Машина движется быстрее мотоцикла.')
    motorcycle_speed += 50
elif car_speed < motorcycle_speed:
    print('Мотоцикл движется быстрее машины.')
else:
    print('Скорости равны')
print()
