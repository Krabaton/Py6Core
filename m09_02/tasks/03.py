"""
Напишите генератор, который возвращает все нечетные квадраты от 0 до предела, используя filter, lambda и map
"""

MAX_VALUE = 10

result = map(lambda x: x ** 2, filter(lambda value: bool(value % 2), list(range(MAX_VALUE))))


def result_generator(limit):
    for i in range(limit):
        value = i ** 2
        if value % 2:
            yield value


result_y = result_generator(MAX_VALUE)

list_result = list(result)
print(list_result)
print(list_result)

print(list(result_y))
print(list(result_y))



