# user_total_expenses = 0
# user_expense = input('Введите сумму расходов за месяц или введите stop для вывода итогов: ')
#
# while user_expense != 'stop':
#     user_expense_float = abs(float(user_expense))
#     user_total_expenses += user_expense_float
#     user_expense = input('Введите сумму расходов за месяц или введите stop для вывода итогов: ')
#
# print(f'Сумма расходов итого: {user_total_expenses}')


shopping_list = []

while True:
    user_goods = input("Введите, покупку или стоп для вывода всего списка покупок: ")
    if user_goods == 'стоп':
        break
    else:
        shopping_list.append(user_goods)

print(shopping_list)
for item in shopping_list:
    print(item)

# [print(item) for item in shopping_list]
