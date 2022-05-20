# Generator as Comprehension

sq_gen = (i ** 2 for i in range(10))
print(sq_gen)

for i in sq_gen:
    print(i, ' ', end='')


# G -> A -> B -> C
