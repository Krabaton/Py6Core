"""
LIFO (англ. last in, first out, «последним пришёл — первым ушёл») — способ организации данных или другими словами
Стек (Stack). В структурированном линейном списке, организованном по принципу LIFO, элементы могут добавляться и
выбираться только с одного конца, называемого «вершиной списка».
Структура LIFO может быть проиллюстрирована следующей картинкой.
"""

from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)


def push(el):
    lifo.appendleft(el)


def pop():
    return lifo.popleft()


push('Volodymyr')
push('Vitaliy')
push('Olexander')
push('Alexandr')
print(lifo)
name = pop()
print(name)
print(lifo)