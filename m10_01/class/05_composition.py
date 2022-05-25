"""
Агрегация
Это когда экземпляр хозяина создается где-то в другом месте кода, и передается в конструктор питомца в качестве параметра
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

    def __init__(self, nickname: str, age: int, owner: Owner) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def get_info(self) -> str:
        return f"It's cat. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


owner = Owner('Yurii', '+380509993524')
cat = Cat('Simon', 4, owner)
print(cat.owner.info())

