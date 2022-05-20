"""
Напишите decorator, который записывает в консоль два сообщения журнала:

: call [количество_время_вызванной_функции]: [имя функции][её аргументы]\n
: result: [имя функции][результат]\n
"""
import sys


def logger(func):
    # BEGIN SOLUTION
    call_count = 0

    def inner(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        sys.stdout.write(f': call [{call_count}]: [{func.__name__}][{args}]\n')
        result = func(*args, **kwargs)
        sys.stdout.write(f': result: [{func.__name__}][{result}]\n')
        return result

    return inner
    # END SOLUTION


@logger
def mul(a, b):
    return a * b


@logger
def add(a, b):
    return a + b


print(mul(4, 8))
print(add(1, 2))
print(mul(7, 6))
print(add(2, 2))
print(add(3, 2))
