def calculate_total_cost(call_duration, from_operator, to_operator, tariffs):
    if (from_operator, to_operator) in tariffs:
        cost_per_minute = tariffs[(from_operator, to_operator)]
        total_cost = cost_per_minute * int(call_duration)
        return total_cost
    print(f'Нет комбинации операторов: {from_operator} -> {to_operator}')
    return False


if __name__ == '__main__':
    actual_tariffs = {
        ('mts', 'mts'): 50,
        ('mts', 'beeline'): 100,
        ('mts', 'megafon'): 150,

        ('beeline', 'mts'): 90,
        ('beeline', 'beeline'): 60,
        ('beeline', 'megafon'): 140,

        ('megafon', 'mts'): 180,
        ('megafon', 'beeline'): 200,
        ('megafon', 'megafon'): 30
    }

    user_call_duration = input('Введите время звонка в минутах: ')
    user_from_operator = input("Укажите своего оператора (MTS/Beeline/Megafon): ").strip().lower()
    user_to_operator = input("Укажите оператора которому вы звоните (MTS/Beeline/Megafon): ").strip().lower()
    user_total_cost = calculate_total_cost(user_call_duration, user_from_operator, user_to_operator, actual_tariffs)
    if user_total_cost:
        print(f'Стоимость вашего разговора составила: {user_total_cost:.2f} рублей')
