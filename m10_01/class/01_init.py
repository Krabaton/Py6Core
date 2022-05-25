"""
Базовые принципы ООП - Инкапсуляция 

Объединение в единое целое данных и алгоритмов обработки этих данных. В рамках ООП данные называются полями объекта, а
функции - объектными методами.
"""


class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


animal = Animal('Simon', 4)
print(animal.nickname)
animal.age = 5
print(animal.get_info())
