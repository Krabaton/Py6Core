string = input('Введите строку')

count_symbols = 0
count_a = 0
count_b = 0
count_c = 0
count_space = 0

# abcddd

for ch in string:
    count_symbols += 1
    if ch == 'a':
        count_a += 1
        continue
    if ch == 'b':
        count_b += 1
        continue
    if ch == 'c':
        count_c += 1
        continue
    if ch == ' ':
        count_space += 1

print(count_symbols, count_space, count_a, count_b, count_c)
