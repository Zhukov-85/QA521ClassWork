def get_total_pait(width, height, consumption=0.2, layers=2):
    total_paint = width * height * consumption * layers
    return round(total_paint, 2)


if __name__ == '__main__':
    print(f'Итого литров краски по умолчанию: {get_total_pait(3, 4)}')
    print(f'Итого литров краски (загустела): {get_total_pait(3, 4, 0.4)}')
    print(f'Итого литров краски (загустела + 3 слоя): {get_total_pait(3, 4, 0.4, 3)}')
    print(f'Итого литров краски (3 слоя): {get_total_pait(3, 4, layers=3)}')
    print(f'Итого литров краски (3 слоя): {get_total_pait(width=3, height=4, layers=3, consumption=0.3)}')
