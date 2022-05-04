import module_b


def foo():
    print("function foo from module a")


module_b.bar()
if __name__ == '__main__':
    foo()
