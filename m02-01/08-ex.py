n = input("Enter a number: ")

max = int(n[0])
min = int(n[0])
sum = 0

# 123456

for char in n:
    num = int(char)
    sum += num
    if num > max:
        max = num
    if num < min:
        min = num


print(max, min, sum)
