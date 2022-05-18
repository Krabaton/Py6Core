# Сделать декоратор, который возвращает кортеж с результатом функции и временем ее выполнения

from time import time, sleep


def time_counter(func):
    def interval(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        passed = time() - start
        return result, passed
    return interval


@time_counter
def test_func(a, b):
    sleep(b)
    return a + b


# print(test_func(3, 1))
# print(test_func(4, 2))


@time_counter
def factorial(n, cache={}):
    if n < 0:
        raise ValueError('Number not be negative')

    def calc(n):
        result = 1
        for val in range(1, n + 1):
            if val in cache:
                result = cache[val]
            else:
                result = val * cache.get(val - 1, 1)
                cache[val] = result
        return result

    return calc(n)


f3 = factorial(1300)
print(f'f3: {f3}')

f5 = factorial(1300)
print(f'f5: {f5}')

print(factorial(4))