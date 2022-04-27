'''
Работа с файлами средствами pathlib
'''

# Текстовый файл
from pathlib import Path
filetext = Path('Temp/my_text_file.txt')

# filetext.write_text('Block text 1')
# filetext.write_text('Block text 2')
# filetext.write_text('Block text 3')
filetext.write_text('Block text 1\nBlock text 2\nBlock text 3')
print(filetext.read_text())

# Бинарный файл bin -> binary
filebin = Path('Temp/my_bin_file.bin')
filebin.write_bytes('Binary data'.encode())  # b'Binary data'
print(filebin.read_bytes().decode())
