'''
Создание директорий pathlib
'''
from pathlib import Path

new_dir = Path('Temporary')
new_dir.mkdir(exist_ok=True)
new_dir.rmdir()

new_dir = Path('Test/Temp')
new_dir.mkdir(exist_ok=True, parents=True)
