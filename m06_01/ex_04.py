'''
Прочитать хвост файла, последние N строк файла. 
Имя файла для чтения передаем как аргумент командной строки
'''
import sys
NUMBER_LINES = 4

if len(sys.argv) != 2:
    print("Передайте имя файла в качестве аргумента командной строки.")
    quit()
