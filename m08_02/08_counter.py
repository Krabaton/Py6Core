"""
Реализовать функцию, которая возвращает n наиболее часто встречающихся и n наименее часто встречающихся чисел из файла
"""

from collections import Counter

filename = 'numbers.txt'


def num_counter(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    counter = Counter([int(i) for i in data.split(',')])
    print(counter)
    ordered = counter.most_common(len(counter))
    print(ordered)
    return [i for i, _ in ordered[:n]], [i for i, _ in ordered[-n:]]


result = num_counter(filename, 10)
a, _ = (10, 5)
print(a)
print(_)
print(result)
