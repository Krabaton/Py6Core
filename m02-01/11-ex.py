num = input()
result = None

try:
    result = 2 / int(num)
except ZeroDivisionError as err:
    print('Деление на ноль')
    print(err)
except ValueError:
    print('Введите число')
else:
    print(result)
