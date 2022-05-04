# from my_package.foo import foo
# from my_package.baz.operation import mul, sum
# from my_package.bar.info import log

# from my_package import foo, mul, sum, log

# print(foo('Taras'))
# print(mul(1, 2))
# print(sum(3, 4))
# log('start proccess')

# ------------------------------------

import my_package as new_package
import requests


def mul(a, b):
    return a * 10


if __name__ == '__main__':
    print(new_package.foo('Taras'))
    print(new_package.mul(1, 2))
    print(new_package.sum(3, 4))
    new_package.log('start proccess')
    print(new_package.log_foo())

# ------------------------------------
# Не используем!!!

# from my_package import *

# print(foo('Taras'))
# print(mul(1, 2))
# print(sum(3, 4))
# log('start proccess')

# joinpath
# 'etc' + '/' + 'dfg'
