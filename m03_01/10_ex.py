print(2 ** 3)


def my_pow(base, exp):
    """
    :param base - основание степени
    :param exp - степень, должна быть больше нуля
    :return base ** exp - результат возведения в степень
    """
    print(base, exp)
    if exp <= 0:
        return 1
    if exp == 1:
        return base
    # 2 * f(2, 2) -> 2 * f(2, 1) -> 2 | 2 * 2 -> 2 * 4 -> 8
    return base * my_pow(base, exp - 1)


# help(my_pow)
# print(my_pow.__doc__)

print(my_pow(2, 3))
