"""
По поводу описания возвращаемого значения в функции при ее описании. Критично ли всегда писать -> None, если функция
ничего не возвращать, особенно в ситуации как в последнем ДЗ когда друг за другом идет набор мелких однотипных функций,
типа 'handle_folder'? И как быть в случаях, если функция возвращает какой-то определенный тип (например int), но также
может завершиться и с возвратом None (например, в качестве сигнала для какого-нибудь особого случая)?
"""

from __future__ import annotations

from typing import TypeVar, Generic

T = TypeVar('T', int, str, None)


def baz(foo: Generic[T]) -> Generic[T]:
    if isinstance(foo, str):  # проверяем что аргумент имеет тип строковый
        return 'Hi world'
    else:
        return foo + 3


def foo(foo: str | int) -> str | int:
    if isinstance(foo, str):
        return 'Hi world'
    else:
        return foo + 3


print(baz('ask'))
print(foo(123))
