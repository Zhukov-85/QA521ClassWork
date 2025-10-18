import csv


def get_sales_data(filepath):
    sales_list = []

    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_list.append(row)
    return sales_list


def analyze_sales(sales):
    total_revenue = 0
    for sale in sales:
        quantity = int(sale['quantity'])
        price = float(sale['price'])
        total_revenue += quantity * price

    return total_revenue


if __name__ == '__main__':
    sales_data = get_sales_data(r'files\sales_data.csv')
    total_sales = analyze_sales(sales_data)
    print(sales_data)
    print(total_sales)
