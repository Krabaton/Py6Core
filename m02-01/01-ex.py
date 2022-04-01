first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    print("The first number is greater than the second number.")
elif first == second:
    print("The first number is equal to the second number.")
else:
    print("The second number is greater than the first number.")


if first % 2:
    print("The first number is odd.")
else:
    print("The first number is even.")


if second % 3:
    print("Число не кратно 3.")
else:
    print("Число кратно 3.")


# if first % 2 or second % 3:
#     print("Первое число четное и второе кратно 3")
# else:
#     print("Первое число не четное или второе не кратно 3")
