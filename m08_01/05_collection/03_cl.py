"""
defaultdict
collections.defaultdict ничем не отличается от обычного словаря за исключением того, что по умолчанию всегда вызывается
функция, возвращающая значение:
"""
from collections import defaultdict

# { key: [], key2: []}
data_d = defaultdict(list)
# data_d[0] = []
data_d[0].append(10)
data_d[0].append(1)
data_d[1].append(100)
print(data_d)

colors = [('yellow', 1), ('blue', 3), ('yellow', 5), ('blue', 10), ('red', 13)]
colors_d = defaultdict(list)
for k, v in colors:
    colors_d[k].append(v)
print(colors_d)


colors = [('yellow', 1), ('blue', 3), ('yellow', 5), ('blue', 10), ('red', 13)]


def my_dict():
    return {}


colors_d = defaultdict(my_dict)
for k, v in colors:
    colors_d[k].update({k + str(v): v})
print(colors_d)


temperatures = [0.5, 0.0, -3.5, 0.0, 2.5, 3.5, 4.0, 0.5, 3.5, 5.5, 6.0, 10.0, 12.5]


def my_add():
    return 5


temperatures_d = defaultdict(my_add)
for i, el in enumerate(temperatures):
    temperatures_d[i] += el

print(list(temperatures_d.values()))
