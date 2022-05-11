"""
Сравнение двух десятичных чисел
Значение 0 указывает, что оба числа равны,
значение 1 указывает, что первое число больше второго числа,
а значение -1 указывает, что первое число меньше второго.
"""
from decimal import Decimal

print(Decimal('1.2').compare(Decimal('1.1')))
print(Decimal('1.0').compare(Decimal('1.1')))
print(Decimal('1.0').compare(Decimal('1.0')))

print(0.1 + 0.2 == 0.3)
num1 = Decimal('0.1') + Decimal('0.2')
num2 = Decimal('0.3')
print(num1.compare(num2))
