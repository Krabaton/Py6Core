# Найдем индекс первого вхождения символа 'а' find()
string = input('String: ')


index = 0

for char in string:
    print(f"Символ: {char} - index = {index}")
    if char == 'a':
        break
    index += 1

print(index)
