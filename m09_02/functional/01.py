# Лямбда функция

def sq_normal(x):
    return x ** 2

# Присваиваем только для примера
sq = lambda x: x ** 2

print(sq_normal(5))
print(sq(5))

print((lambda: 'TODO FIX IT')())
