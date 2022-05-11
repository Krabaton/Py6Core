"""
Какое минимальное количество раз вы должны подбросить монетку, чтобы три раза подряд 
выпал либо орел, либо решка?
random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
"""

import random

d = {
    1: 'Орел',
    2: 'Решка'
}
count_O = 0
count_P = 0
sequence = []

while count_P < 3 and count_O < 3:
    trial = random.randint(1, 2)
    if trial == 1:
        count_O += 1
        count_P = 0
    else:
        count_O = 0
        count_P += 1
    sequence.append(d[trial])

print(f"Получена последовательность: {sequence}")
if count_O == 3:
    print("Выпало три орла подряд")
else:
    print("Выпало три решки подряд")

print(f'Количество попыток {len(sequence)}')
