
class Singleton:
    instance = None

    def __new__(cls, *args):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, value):
        self.value = value


foo = Singleton(10)
baz = Singleton(20)  # baz = foo -> __init__()
bar = Singleton(30)

print(foo.value, baz.value, bar.value)
print(foo, baz, bar)
