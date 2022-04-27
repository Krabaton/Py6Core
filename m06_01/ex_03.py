'''
Прочитать первые N строк файла. 
Имя файла для чтения передаем как аргумент командной строки
'''

import sys
NUMBER_LINES = 4

if len(sys.argv) != 2:
    print('Необходимо передать только имя файла для чтения!')
    quit()

try:
    file = open(sys.argv[1], 'r', encoding='utf-8')
    line = file.readline()
    count = 0
    while count < NUMBER_LINES and line != '':
        line = line.strip()
        count += 1
        print(line)
        line = file.readline()
    file.close()
except OSError as err:
    print(f'Ошибка доступа к файлу: {err}')
