"""
Ассоциация
Это когда один класс включает в себя другой класс в качестве одного из полей. Ассоциация описывается словом «имеет».
Животное имеет хозяина.

Выделяют два частных случая ассоциации: композицию и агрегацию.

Композиция
Это когда хозяин не существует отдельно от питомца. Он создается при создании питомца и полностью управляется питомцем.
"""


class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


class Owner:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat(Animal):

    def __init__(self, nickname: str, age: int, name: str, phone: str) -> None:
        super().__init__(nickname, age)
        self.owner = Owner(name, phone)

    def get_info(self) -> str:
        return f"It's cat. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


cat = Cat('Simon', 4, 'Yurii', '+380509993524')
print(cat.owner.info())