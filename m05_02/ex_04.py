'''
Метод: split

Напишем универсальную функцию get_parameters которая будет возвращать словарь с данными. Поскольку в первой строке разделить символ ; а во второй &, поэтому здесь удачно подойдет случай (a|b - соответствует a или b)
'''

import re


url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"  # ;

url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"  # &


def get_parameters(data: list) -> dict:
    obj_query = {}
    for el in data:
        key, value = el.split('=')
        obj_query.update({key: value.replace('+', ' ')})
    return obj_query


data = re.split(r';|&', url_query)
print(get_parameters(data))
data = re.split(r';|&', url_search)
print(get_parameters(data))
