'''
Чтение и запись в файл.
'''

file = open('test.txt', 'w', encoding='utf-8')
file.write('Hello world!\n')
file.write('Hello Ukraine!\n')
file.writelines(['Hi Bob!\n', 'Hi Dima!\n', 'Test', 'ups\n'])
file.close()

file = open('test.txt', 'r', encoding='utf-8')
# result = file.read()
# result = file.readline()
result = file.readlines()
print(result)
file.close()
