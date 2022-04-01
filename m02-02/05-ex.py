# Найдем индекс первого вхождения символа 'а' find()
string = input('String: ')

index = -1
count = 0

for char in string:
    if char == 'a':
        index = count
    print(f"Символ: {char} - index = {index} : count = {count}")
    count += 1

print(index)
