# weather = input("Какая сегодня погода: 1 - солнечно/2 - дождь ")
#
# if weather == '1':
#     print('Возьми с собой очки.')
#     # print('Хорошего дня!')
# elif weather == '2':
#     print('Возьми с собой зонт.')
#     # print('Хорошего дня!')
# else:
#     print('Неизвестная команда.')
#
# print('Хорошего дня!')

# counter = 0
# while counter < 5:
#     print("inside cycle")
#     counter += 1
# print()
#
# for i in range(5):
#     print(f"inside cycle - {i}")
# print()
#
# item_list = ['item_1', 'item_2', 'item_3']
# for item in item_list:
#     print(item)
# print()

try:
    print('Провокация')
    print(1 / 0)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except:
    print('То или иное исключение в зависимости от возможной ошибки')
else:
    print('Выполняем если исключения не было')
finally:
    print('Выполняется в любом случае')


def some_function():
    print("Внутри функции")
    if True:
        pass


class ExampleClass:
    def __init__(self, attr):
        self.attr = attr

    def some_method(self):
        print(self.attr)

    def __str__(self):
        return "Класс для примера по блокам выполнения."
