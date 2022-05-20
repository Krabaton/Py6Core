# Filter

payment = [100, -3, 400, 35, -100]


def is_negative_number(num) -> bool:
    if num < 0:
        return True

    return False


p_values = filter(is_negative_number, payment)
print(list(p_values))


p_values = filter(lambda num: num > 0, payment)
print(list(p_values))

