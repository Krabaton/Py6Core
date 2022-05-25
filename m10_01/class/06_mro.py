"""
Method Resolution Order (MRO).
MRO в Python работает следующим образом:

1. Ищет атрибут среди аттрибутов самого класса. Именно благодаря этому, вы можете "переопределять" родительские атрибуты.
2. Ищет атрибут у первого родителя (тот, что указан первым в списке родителей).
3. Ищет атрибут у следующего родителя в списке родителей, пока такие есть.
4. Ищет атрибут в родителях первого родителя.
5. Повторяет п.4 для всех родителей.
6. Вызывает исключение, что атрибут не найден.
"""


class A:
    x = 'a'


class B(A):
    x = 'b'


class C(A):
    x = 'c'


class D(C, B):
    def get_x(self):
        return D.x


print(D.__mro__)

d = D()
d.get_x()

