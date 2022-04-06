def modeling(factor, *_, correction=0.5):
    return factor * correction


print(modeling(5, 3, 2, 1))
print(modeling(5, 3, 2, 1, correction=3))
print(modeling(2, correction=3))


def model(factor, correction=0.5):
    return factor * correction


print(model(5, 3))
