"""
Методы: split, replace
----
Распарсиваем query запрос для гугла. Здесь классический разделитель & и превращаем в словарь с данными
"""

url_search = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

_, query = url_search.split('?')

print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})

print(obj_query)
