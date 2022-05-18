#  Декоратор с названием

def decorator_with_name(name):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(f'Decorator: {name}')
            result = func(*args, **kwargs)
            return result
        return inner
    return wrapper


@decorator_with_name('Big decorator')
def adder(x, y):
    return x + y


@decorator_with_name('Small decorator')
def mul(x, m=10):
    return x * m
# mul = decorator_with_name('Small decorator')(mul)


if __name__ == '__main__':
    print(adder(3, 4))
    print(mul(3, m=3))
    print(mul(3))
