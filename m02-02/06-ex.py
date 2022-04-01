BASE = 2

num = int(input('Введите целое число: '))

result = ""
q = num

#  --------

r = q % BASE
result = str(r) + result
q = q // BASE

# ---------

while q > 0:
    r = q % BASE
    result = str(r) + result
    q = q // BASE


print(f"{num} -> {result}")
