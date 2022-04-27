'''
Добавим запись в файл
'''

file = open('test.txt', 'a', encoding='utf-8')  # append
file.write('The end!\n')
file.write('It still end!\n')
file.close()
