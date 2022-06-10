"""
Интерпретатор Python ленивый и если его явно не попросить создать копию объекта, он создаст новый указатель на всё тот
же объект. Не всегда такое поведение приветствуется. Для того чтобы создать копию объекта в пакете copy есть функции:
- copy -- поверхностная копия
- deepcopy -- глубокая копия.
"""
from copy import copy, deepcopy

l = [1, 2, 3, ["a", "b", "c"]]
test_l = l[:]

l_copy = copy(l)
l_deep = deepcopy(l)

print(l == l_copy, l is l_copy)

l[0] = 9
print(l, l_copy, l_deep)
l[3][0] = 'd'
l_deep[3][2] = 'f'
print(l, l_copy, l_deep)
print(test_l)
