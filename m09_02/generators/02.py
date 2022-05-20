# Самостоятельный вызов через next

def simple_gen():
    yield 'First'
    yield 'Second'


gen = simple_gen()
print(gen)

r = next(gen)
print(r)

r = next(gen)
print(r)

r = next(gen)
print(r)
