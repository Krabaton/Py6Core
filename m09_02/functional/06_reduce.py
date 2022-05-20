# reduce
from functools import reduce

numbers = [5, 6, 7]

sum_nums = reduce(lambda x, y: x + y, numbers, 0)
print(sum_nums)

mul_nums = reduce(lambda x, y: x * y, numbers, 1)
print(mul_nums)

greeting = reduce(lambda calc, next: calc + next, ['H', 'e', 'l', 'l', 'o'], '')
print(greeting)
