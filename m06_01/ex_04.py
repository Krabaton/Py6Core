'''
Прочитать хвост файла, последние N строк файла. 
Имя файла для чтения передаем как аргумент командной строки
'''
import sys
NUMBER_LINES = 4

if len(sys.argv) != 2:
    print("Передайте имя файла в качестве аргумента командной строки.")
    quit()

try:
    lines = []
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        for line in file:  # file.readline()
            lines.append(line)
            if len(lines) > NUMBER_LINES:
                lines.pop(0)

    print(lines)

except OSError as err:
    print(f'Ошибка доступа к файлу: {err}')
