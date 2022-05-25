"""
Базовые принципы ООП - Наследование 

Наследование есть свойство объектов порождать своих потомков. Объект-потомок автоматически наследует от родителя все
поля и методы, может дополнять объекты новыми полями и заменять (перекрывать) методы родителя или дополнять их.
"""


class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


class Cat(Animal):
    name = ['Cat']

    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


cat = Cat('Simon', 4, 'Yurii')
print(cat.nickname)
cat.age = 5
print(cat.get_info())
print(cat.sound())
# print(cat.name)
# cat2 = Cat('Boris', 10, 'Sergey')
# cat2.name[0] ='Boris Animal'
# print(cat2.name)
# print(cat.name)
# print(Cat.name)
print(dir(cat))