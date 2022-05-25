from collections import UserList
from random import randint


class MyList(UserList):
    _info = "Этой мой класс списка!!!"

    def get_positive(self):
        return list(filter(lambda x: x >= 0, self.data))

    def get_negative(self):
        return list(filter(lambda x: x < 0, self.data))

    def info(self):
        return self._info


r = []
for _ in range(0, 20):
    r.append(randint(-5, 5))

results = MyList(r)  # results = []

print(results)
print(results.get_positive())
print(results.get_negative())
print(results.info())
print(MyList.__mro__)

