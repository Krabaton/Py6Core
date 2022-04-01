#  Проверить  3-х значное число палиндром?

num = int(input('Number: '))

n1 = num // 100
n2 = num % 10

if n1 == n2:
    print('Yes')
else:
    print('No')
