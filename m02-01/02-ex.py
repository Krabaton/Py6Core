num = int(input("Enter the first number: "))
print(num)
length = len(str(num))


if length == 2 and num % 2 == 0:
    print("Четное двухзначное число")
else:
    print("Нет")
