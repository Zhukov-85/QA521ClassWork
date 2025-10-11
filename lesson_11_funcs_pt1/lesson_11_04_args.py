# функция для подсчета некой суммы с налогом
def get_total_with_tax(value, tax_percentage):
    """
    :param value: налоговая база
    :param tax_percentage: процент налога
    :return: сумма с налогом
    """
    total = (value / (100 - tax_percentage)) * 100
    return total


def get_total_salaries_list(salaries_list: list[int], tax_percentage: float, tax_calc_func) -> list[float]:
    # salaries_list = employees_salaries_list
    # tax_percentage = income_tax
    # tax_func = get_total_with_tax   !БЕЗ СКОБОК!
    """
    :param salaries_list:
        list - список с зарплатами сотрудников
    :param tax_percentage:
        float - налоговая ставка
    :param tax_calc_func:
        func - функция для подсчета суммы с налогом
    :return:
        list - список зарплат сотрудников с налогом
    """
    total_salaries_list = []
    for salary in salaries_list:
        total = tax_calc_func(salary, tax_percentage)
        total_salaries_list.append(round(total, 2))
    return total_salaries_list


if __name__ == '__main__':
    # income = float(input('Введите сумму дохода: '))
    # income_tax = float(input("Введите процент налога: "))
    # print(f'Сумма с налогом: {get_total_with_tax(income, income_tax)}')
    # print(get_total_with_tax)
    employees_salaries_list = [50000, 60000, 70000, 55000]
    income_tax = 13
    emp_total_salaries_list = get_total_salaries_list(employees_salaries_list, income_tax, get_total_with_tax)
    print(emp_total_salaries_list)
