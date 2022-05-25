"""
Базовые принципы ООП - Полиморфизм 

Полиморфизм - это свойство родственных объектов (т.е. объектов, имеющих одного общего родителя) решать схожие по смыслу
проблемы разными способами.
"""

class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


class Cat(Animal):

    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def get_info(self) -> str:
        return f"It's cat. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


class Dog(Animal):

    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def get_info(self) -> str:
        return f"It's dog. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Woof!"


cat = Cat('Simon', 4, 'Yurii')
dog = Dog('Alisa', 7, 'Vlad')

for el in (cat, dog):
    if type(el) is Dog:
        print(f"{el.sound()} {el.get_info()}")

print('--------------------')
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(isinstance(dog, Dog))
print('--------------------')
print(type(dog) is Animal)
print(type(dog) is Dog)
print('------------------')

print(dog.get_info())
print(super(Dog, dog).get_info())