# Создание Decimal из вещественных чисел

from decimal import Decimal

num1 = 1.37
num2 = 1.5

f = Decimal.from_float(num1)
s = Decimal.from_float(num2)

print(f, s)

f = Decimal(str(num1))
s = Decimal(str(num2))

print(f, s)
