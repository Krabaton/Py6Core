'''
Больше возможностей pathlib
'''
from pathlib import Path

current_dir = Path('.')

# Проверка свойств файлов
# for el in current_dir.iterdir():
#     print(f'{el.name}. Dir: {el.is_dir()}. File: {el.is_file()}. Exist: {el.exists()}')

# Проверка не существующего файла
file = current_dir / 'bin' / 'utils' / 'paint.drawio.svg'
# print(file.exists())

#  Поиск по шаблону
for el in current_dir.glob('**/*.jpg'):
    print(el)

# Удаление файла
tmp = Path('empty.txt')
if tmp.exists():
    tmp.unlink()
