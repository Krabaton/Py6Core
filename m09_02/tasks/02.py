"""
Генератор возврата, который возвращает целое число между min_val и max_val в бесконечном цикле
"""

from random import randint, seed


def cycle_random_gen(min_val, max_val):
    # BEGIN SOLUTION
    seed()
    while True:
        yield randint(min_val, max_val)
    # END SOLUTION


rand_gen = cycle_random_gen(5, 15)

result = []
for _ in range(20):
    value = next(rand_gen)
    result.append(value)

print(result)


result_2 = []
for _ in range(10):
    value = next(rand_gen)
    result_2.append(value)

print(result_2)
