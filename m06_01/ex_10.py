'''
Запись в файл байтовых строк. Работа с разными кодировками
'''

from pathlib import Path

message = "Привет мир! Hello world!"
print(message.encode())  # UTF-8
print(message.encode('utf-16'))
print(message.encode('cp1251'))
print(b'\xcf\xf0\xe8\xe2\xe5\xf2 \xec\xe8\xf0!'.decode('cp1251'))
folder = Path('Test')

#  Save binary
with open(folder / 'utf-8.txt', 'wb') as f:
    f.write(message.encode())

with open(folder / 'utf-16.txt', 'wb') as f:
    f.write(message.encode('utf-16'))

with open(folder / 'cp1251.txt', 'wb') as f:
    f.write(message.encode('cp1251'))

#  Read
with open(folder / 'utf-8.txt', 'rb') as f:
    print(f.read().decode())

with open(folder / 'utf-16.txt', 'rb') as f:
    print(f.read().decode('utf-16'))

with open(folder / 'cp1251.txt', 'rb') as f:
    print(f.read().decode('cp1251'))
