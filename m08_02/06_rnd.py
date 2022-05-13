"""
Генерация автомобильного знака. Две буквы, четыре цифры, две буквы.
Для Kиeвскaя облacть код АI
Последние две буквы из списка: A, B, C, E, H, I, K, M, O, P, T, X
(використовуються українські літери, що мають графічні відповідники у латиниці)
"""

import random

start = "AI"
set_of_letters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]
set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

numbers = "".join(random.choices(set_of_numbers, k=4))
print(random.choices(set_of_numbers, k=4))
last_l = "".join(random.choices(set_of_letters, k=2))

print(f'{start} {numbers} {last_l}')
