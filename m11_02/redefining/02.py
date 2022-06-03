"""
Реализовать класс-список (list) в котором умножение переопределено как скалярное умножение векторов
"""

from collections import UserList


class MulArray(UserList):
    def __init__(self, *args):
        self.data = list(args)

    def __mul__(self, other):
        res = 0
        for i in range(min(len(self.data), len(other))):
            res += self.data[i] * other[i]
        return res

    def __rmul__(self, other):
        res = 0
        for i in range(min(len(self.data), len(other))):
            res += self.data[i] * other[i]
        return res


vec1 = MulArray(1, 2, 3)
vec2 = MulArray(3, 4, 5)

print(vec1 * vec2)
print(vec1 * [3, 3, 3])
print(vec2 * [1, 1, 1])
print([1, 1, 1] * vec2)
