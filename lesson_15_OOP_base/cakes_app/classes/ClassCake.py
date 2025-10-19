class CakeForm:

    def __init__(self, dough, form, *args):
        self.dough = dough
        self.form = form
        if not args:
            self.ingredient_list = []
        else:
            self.ingredient_list = list(args)

    def make_dough(self):
        return f'Мы замешиваем тесто: {self.dough}'

    def make_form(self):
        return f'Мы выкладываем тесто в форму: {self.form}'

    def add_ingredient(self, ingredient):
        self.ingredient_list.append(ingredient)
        return f'Добавлен: {ingredient}'

    def add_ingredients(self, *args):
        self.ingredient_list.extend(args)
        return f'Добавлены: {', '.join(args)}'

    def cook_cake(self, time=40):
        if self.ingredient_list:
            if time > 80:
                return f'За {time} минут кекс из теста: {self.dough}, формы: {self.form}, дополнительно: {', '.join(self.ingredient_list)} сгорит :('
            return f'Мы выпекаем кекс из теста: {self.dough}, формы: {self.form}, дополнительно: {', '.join(self.ingredient_list)} {time} - минут'
        else:
            if time > 80:
                return f'За {time} минут кекс из теста: {self.dough}, формы: {self.form} сгорит :('
            return f'Мы выпекаем кекс из теста: {self.dough}, формы: {self.form} {time} - минут'

    def __str__(self):
        if self.ingredient_list:
            return f'Кекс из теста: {self.dough}. Форма: {self.form}. Дополнительно: {', '.join(self.ingredient_list)}'
        return f'Кекс из теста: {self.dough}. Форма: {self.form}. Без начинки'
