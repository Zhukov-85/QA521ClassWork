class CakeForm:

    def __init__(self, dough, form):
        self.dough = dough
        self.form = form
        # print(f'Я кекс из теста: {self.dough}. Моя форма: {self.form}.')

    def __str__(self):
        return f'Я кекс из теста: {self.dough}. Моя форма: {self.form}.'


if __name__ == '__main__':
    cake_1 = CakeForm('Пшеничное', 'Круглая')
    cake_2 = CakeForm('Имбирное', 'Квадратная')
    print(cake_1)
    print(cake_2)
    print(cake_1.dough)
    #       self.dough
    print(cake_1.form)
    print(cake_2.dough)
    print(cake_2.form)
