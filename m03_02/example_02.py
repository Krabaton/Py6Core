def main():
    value = int(input('Введите целое число: '))
    if (is_prime(value)):
        print(f'{value} - простое число')
    else:
        print(f'{value} - не простое число')


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
