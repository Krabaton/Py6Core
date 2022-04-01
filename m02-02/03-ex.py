string = input('String: ')

count = 0

for char in string:
    if char == 'a':
        count += 1
    print(f"Символ: {char} - count = {count}")

print(count)
# ----
print(string.count('a'))
