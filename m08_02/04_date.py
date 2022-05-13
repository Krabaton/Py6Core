"""
Напишите функцию, принимающую на вход три 
целых числа: день, месяц и год. Функция должна возвращать порядковый
номер заданного дня в указанном году.

Результат функции: номер года и порядковый номер дня в этом
году – оба в целочисленном формате.
"""

from datetime import datetime, date


def transform_to_ordinal_date(day, month, year):
    d = date(year, month, day).toordinal()
    diff = d - date(year, 1, 1).toordinal() + 1
    return year, diff


print(transform_to_ordinal_date(19, 1, 2022))
print(transform_to_ordinal_date(31, 12, 2022))

"""
Разработайте функцию, принимающую в качестве единственного параметра порядковую дату, включающую в себя год и день 
по порядку. В качестве результата функция должна возвращать день и месяц, соответствующие переданной порядковой дате.
"""


def transform_to_date(ordinal, year):
    d1 = date(year, 1, 1).toordinal()
    d = datetime.fromordinal(d1 - 1 + ordinal)
    return d


print(transform_to_date(99, 2001))
print(transform_to_date(365, 2022))
