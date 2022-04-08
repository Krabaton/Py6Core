# fn('+') -> sum  fb('*') -> mul

def collector(operation: str):
    result = None
    if operation == '+':
        result = 0
    if operation == '*':
        result = 1
    if result is None:
        return "Функция не поддерживает операцию"

    value = input('Введите целое число: ')
    while True:
        if value == '':
            break
        if operation == '+':
            result = result + int(value)
        if operation == '*':
            result = result * int(value)
        value = input('Введите целое число: ')

    return result


result = collector('+')
# 3, 4, '' -> 7
print(result)

result = collector('*')
# 3, 4, '' -> 12
print(result)

result = collector('-')
# 3, 4, '' -> 12
print(result)
