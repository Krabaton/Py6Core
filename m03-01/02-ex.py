count = 0


def foo():
    count = 0
    count = count + 5
    return count


def baz():
    global count
    count = count + 1
    return count


print(f"Function foo: {foo()}")
print(f"Global: {count}")
print(f"Function baz: {baz()}")
print(f"Global: {count}")
