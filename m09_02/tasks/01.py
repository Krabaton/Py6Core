"""
Напишите decorator, который записывает в консоль два сообщения журнала:

: call [количество_время_вызванной_функции]: [имя функции][её аргументы]\n
: result: [имя функции][результат]\n
"""

import sys


def logger(func):
    # BEGIN SOLUTION
    ...
    # END SOLUTION


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


mul(4, 8)
add(1, 2)
mul(7, 6)
add(2, 2)
add(3, 2)
