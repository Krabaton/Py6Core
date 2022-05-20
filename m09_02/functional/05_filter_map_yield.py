# map, filter, generator

MAX_VALUE = 16

result = map(lambda x: x ** 2, filter(lambda value: bool(value % 2), [i for i in range(1, MAX_VALUE)]))


def result_generator(limit):
    for i in range(1, limit):
        value = i ** 2
        if value % 2:
            yield value


result_y = result_generator(MAX_VALUE)

list_result = list(result)
print(list_result)
print(list_result)

print(list(result_y))
print(list(result_y))
