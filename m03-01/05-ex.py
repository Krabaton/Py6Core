
# tuple
# foo: tuple = (1, 4, "baz")
# print(foo)

# # dict
# bar: dict = {
#     "Zina": 16,
#     "Aleksandr": 23
# }
# print(bar["Zina"])


def first(size, *args):
    print(f"size: {size}")
    print(f"args: {args} его длина {len(args)}")


result = first(12, 2, 3, 4, 5, 'Hello', 27)


def second(size, **kwargs):
    print(f"size: {size}")
    print(f"args: {kwargs} его длина {len(kwargs)}")


result = second(12, foo=3, baz="hi")


def third(size, *args, **kwargs):
    print(f"size: {size}")
    print(f"args: {args} его длина {len(args)}")
    print(f"args: {kwargs} его длина {len(kwargs)}")


third(12, 2, 3, 4, 5, 'Hello', 27, foo=3, baz="hi")
