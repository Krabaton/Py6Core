"""
collections.deque(iterable, [maxlen]) - создаёт очередь из итерируемого объекта с максимальной длиной maxlen. Очереди очень похожи на списки, за исключением того, что добавлять и удалять элементы можно либо справа, либо слева.

Методы, определённые в deque:

append(x) - добавляет x в конец.

appendleft(x) - добавляет x в начало.

clear() - очищает очередь.

count(x) - количество элементов, равных x.

extend(iterable) - добавляет в конец все элементы iterable.

extendleft(iterable) - добавляет в начало все элементы iterable (начиная с последнего элемента iterable).

pop() - удаляет и возвращает последний элемент очереди.

popleft() - удаляет и возвращает первый элемент очереди.

remove(value) - удаляет первое вхождение value.

reverse() - разворачивает очередь.

rotate(n) - последовательно переносит n элементов из конца в начало (если n отрицательно, то наоборот).
"""
from collections import deque

l = list(range(1, 10))
l_deque = deque(l)
print(l_deque)
l_deque = deque(l, 5)
print(l_deque)

l_deque.appendleft(10)
l_deque.append(11)
print(l_deque)
print(l_deque.count(10))
print(l_deque.index(6))

l_deque.rotate(2)
print(l_deque)

l_deque.reverse()
print(l_deque)
