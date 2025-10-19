class CakeForm:

    def make_dough(self):
        return 'Мы замешиваем тесто'

    def make_form(self):
        return 'Мы выкладываем тесто в форму'

    def cook_cake(self, time=40):
        if time > 80:
            return f'За {time} минут кекс сгорит'
        return f'Мы выпекаем тесто {time} минут.'


if __name__ == '__main__':
    cake_1 = CakeForm()
    cake_2 = CakeForm()

    # print(cake_1 is cake_2)
    # print(id(cake_1), id(cake_2))
    # cake_3 = cake_1
    # print(cake_1 is cake_3)

    print(cake_1.make_dough())
    print(cake_1.make_form())
    print(cake_1.cook_cake())
    print()
    print(cake_2.make_dough())
    print(cake_2.make_form())
    print(cake_2.cook_cake(100))

