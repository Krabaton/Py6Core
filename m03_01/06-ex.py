def sum(start, *args):
    sum = start
    for el in args:
        sum = sum + el
    return sum


result = sum(2, 3, 5, 1)
print(result)
result = sum(2, 3, 5, 1, 3, 5, 1)
print(result)
