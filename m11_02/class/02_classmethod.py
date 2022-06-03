"""
    Разбираем разницу между: обычным методом, @classmethod и @staticmethod
"""


class DecoratorTest:

    def doubler(self, x):  # self == decor
        print('Mul on 2: %s' % self)
        return x * 2

    @classmethod
    def triples(cls, x):  # cls == DecoratorTest
        print('Mul on 3: %s' % cls)
        return x * 3

    @staticmethod
    def quad(x):
        print('Mul on 4')
        return x * 4


decor = DecoratorTest()
print('---Экземпляр класса---')
print(decor.doubler(4))
print(decor.triples(4))
print(decor.quad(4))
print('---Вызов через класс---')
print(DecoratorTest.triples(4))
print(DecoratorTest.quad(4))

print(f'Test: {10} {"test"}')
