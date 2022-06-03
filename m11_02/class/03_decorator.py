# Декораторы классов

def method_decorator(func):
    def wrapper(self, *args):
        print('---Decorator run--')
        result = func(self, *args)
        print('---Decorator end--')
        return result
    return wrapper


def class_decorator(cls):
    print('---Decorator class---')
    new_cls = cls
    new_cls.value = 42
    return new_cls


@class_decorator
class TestClass:
    name = 'TestClass'

    @method_decorator
    def info(self, user):
        return f'Hello {user}. This is {self.name}'


t = TestClass()
print(t.info('Oleksandr'))
print(t.value)
t.test = 10
print(t.test)
