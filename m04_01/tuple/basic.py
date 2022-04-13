from turtle import circle


my_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100)

print(my_tuple[3])

print(my_tuple[3:])

print(list(my_tuple))

circle = {
    (0, 0): "Центр окружности",
    (1, 0): "0 или 360 градусов",
    (0, 1): "90 градусов",
    (-1, 0): "180 градусов",
    (0, -1): "270 градусов",
}

print(circle.get((1, 0)))

baz = 10
foo = -1

baz, foo, *rest = foo, baz, 100, 40

print(baz, foo)
print(rest)
