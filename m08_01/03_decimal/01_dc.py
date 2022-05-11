"""
Необходимость использования. Настройка точности
"""

from decimal import Decimal, getcontext

f = 0.2 + 0.1 + 0.3 - 0.5
print(f)

rf = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
print(rf)

not_precision = Decimal('1') / Decimal('3')
print(not_precision)

getcontext().prec = 6
precision = Decimal('1') / Decimal('3')
print(precision)
precision = Decimal('11') / Decimal('3')
print(precision)