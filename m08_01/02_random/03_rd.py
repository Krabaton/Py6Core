"""
Какое минимальное количество раз вы должны подбросить монетку, чтобы три раза подряд 
выпал либо орел, либо решка?
random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
"""

import random

O = 1  # Орел
P = 2  # Решка
count_O = 0
count_P = 0
sequence = []


print(f"Получена последовательность: {sequence}")
if count_O == 3:
    print("Выпало три орла подряд")
else:
    print("Выпало три решки подряд")

print(f'Количество попыток {len(sequence)}')
