# Простейший генератор

def simple_gen():
    yield 'First'
    yield 'Second'


for r in simple_gen():
    print(r)
