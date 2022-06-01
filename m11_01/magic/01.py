# Методы: __new__ и __init__

class Foo:  # class Foo(object):
    def __new__(cls, *args):
        print('Метод new Foo')
        print(args)
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print('Конструктор Foo')
        self.value = value


# class Baz(Foo):
#     def __init__(self, value):
#         print('Конструктор Baz')
#         super().__init__(value)


baz = Foo(10)  # __new__() -> __init__()
bar = Foo(20)

print(baz.value, bar.value)
print(baz, bar)
