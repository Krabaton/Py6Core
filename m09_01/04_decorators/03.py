# Пример Декоратора без *args, **kwargs
def decorator_name(func):
    def wrapper(*args):
        result = func(*args)  # func == full_name
        print('Good bye!')
        return result

    return wrapper


def prefix_decorator_name(func):
    def wrapper(*args):
        print('Prefix!', args)
        name, surname = args
        name = f'Mr. {name}'
        result = func(name, surname)  # func = decorator_name -> wrapper
        print('Prefix end -----------')
        return result

    return wrapper


@prefix_decorator_name
@decorator_name
def full_name(name, surname):
    print(f'Hello {name} {surname}!')


full_name('Николай', 'Зырянов')
