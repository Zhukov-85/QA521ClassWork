from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name
        pass

    @abstractmethod
    def eat(self, food):
        pass


class Cat(Animal):

    def __init__(self, name, age):
        # self.name = name
        super().__init__(name)
        self.age = age

    def eat(self, food):
        print(f'Кот {self.name} возрастом {self.age} кушает {food}')


if __name__ == '__main__':
    cat_01 = Cat('Барсик', 3)
    cat_01.eat('рыба')
    cat_01.eat('мясо')

    cat_02 = Cat('Мурзик', 5)
    cat_02.eat('курица')
