
# Функция как объект первого класса

# Второе требование - функция может быть передана в другую функцию как аргумент

def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def ops(a, b, func):
    return func(a, b)


result = ops(2, 3, mul)
print(result)

result = ops(2, 3, add)
print(result)
