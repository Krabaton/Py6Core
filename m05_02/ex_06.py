'''
Метод: sub

Дана строка символов.
Исключить из этой строки группы символов, расположенные между скобками [, ].
Сами скобки тоже должны быть исключены.
Пред
'''

import re

string = "Исключить из этой [строки группы] символов, [расположенные между] скобками [, ]."

# Квантификатор ? повторения изменяет поведение поиска на не жадное
print(re.findall(r'\[.*?\]', string))

sanitize_string = re.sub(r'\[.*?\]', '', string)
print(sanitize_string)

sanitize_string = re.sub(r'\[|\]', '', string)
print(sanitize_string)

sanitize_string = re.sub(r'\[.*?\]', '[]', string)
print(sanitize_string)
