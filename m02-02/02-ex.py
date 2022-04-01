#  Проверить  3-х значное все ли цифры разные? Если только две одинаковые цифры?

num = input('Number: ')


if len(num) != 3:
    print('Введите трехзначное число')
else:
    n1 = int(num) // 100  # 234 -> 2
    n2 = int(num) // 10 % 10  # 234 -> 23 -> 3
    n3 = int(num) % 10  # 234 -> 4

    print(n1, n2, n3)

    if n1 != n3 and n2 != n3 and n2 != n1:
        print('Все цифры разные')

    if (n1 == n3 or n2 == n3 or n2 == n1) and not (n1 == n2 and n1 == n3):
        print('Если только две одинаковые цифры')

print('End program')
