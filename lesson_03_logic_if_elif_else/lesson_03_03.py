# num_1 = 1
# num_2 = 2
# num_3 = 3
#
# print(num_2 > num_1 and num_3 > num_2)
# print(num_1 < num_2 < num_3)
# print(num_3 > num_2 > num_1)

competent = True
responsible = True
print(competent and responsible)

competent = True
responsible = False
print(competent and responsible)
print()

competent = True
responsible = True
print(competent or responsible)

competent = True
responsible = False
print(competent or responsible)

competent = False
responsible = False
print(competent or responsible)
print()

previosly_fired = True
print(not previosly_fired)

previosly_fired = False
print(not previosly_fired)
