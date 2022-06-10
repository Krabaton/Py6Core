# Под капотом функции copy, deepcopy делают не более, чем вызывают методы __copy__, __deepcopy__.

from collections import UserList
from copy import copy, deepcopy


class CopyList(UserList):
    def __init__(self, *data):
        super().__init__()
        self.data = list(data)

    def __copy__(self):
        n = CopyList()
        n.data = self.data
        return n

    def __deepcopy__(self, memodict={}):
        n = CopyList()
        memodict[id(self)] = n  #
        for el in self.data:
            n.append(deepcopy(el, memodict))
        # Словарь memo хранит в качестве ключей id объектов и сами объекты как значения, чтобы не было рекурсии при
        # копировании
        return n


data = CopyList([1, 2, 3, 4])
data_copy = copy(data)
data_deep = deepcopy(data)

print(id(data), data)
print(id(data_copy), data_copy)
print(id(data_deep), data_deep)

print(id(data[0]), data[0])
print(id(data_copy[0]), data_copy[0])
print(id(data_deep[0]), data_deep[0])