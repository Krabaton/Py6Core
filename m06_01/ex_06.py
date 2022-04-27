'''
Основные возможности pathlib
'''

from pathlib import Path

current_path = Path('.')
# print(current_path)
# print(current_path.cwd())

# Путь
file = current_path / 'bin' / 'utils' / 'paint.drawio.svg'
print(file)
# print(current_path.joinpath('bin', 'utils', 'paint.drawio.svg'))

# Части файла
print(file.parts)

# Имя файла
print(file.name)
print(file.name.split('.')[0])

# Родительская папка
print(file.parent)

# Суффикс
print(file.suffix)
print(file.suffixes)
