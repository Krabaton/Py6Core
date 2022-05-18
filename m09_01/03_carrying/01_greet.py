# Карринг — это преобразование функции от многих аргументов в набор функций, каждая из которых является
# функцией от одного аргумента. Мы можем передать часть аргументов в функцию и получить обратно функцию,
#  ожидающую остальные аргументы.

def greeting_simple(name, msg):
    return f"{name} - {msg}"


print(greeting_simple('Boris', 'Go to work!'))
print(greeting_simple('Boris', 'Go to home!'))


def greeting(name):
    def message(msg):
        return f'{name} - {msg}'

    return message


msg_for_boris = greeting('Boris')

print(msg_for_boris('Go to home!'))
print(msg_for_boris('Go to work!'))



