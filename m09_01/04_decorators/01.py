# Декораторы
# Шаблон проектирования, который заключается в том, чтобы расширять существующий функционал,
# не внося изменений в код этого самого функционала.


def greeting(val):
    print(f'My name is {val}!')


def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        print('Hello!')
        result = func(*args, **kwargs)
        print('Good bye!')
        return result

    return wrapper


greeting('Bot')

change_greeting = greeting_decorator(greeting)
change_greeting('Bot')
