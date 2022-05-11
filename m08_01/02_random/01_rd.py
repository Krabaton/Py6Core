import random

random.seed()

print(random.random())
print(random.randint(1, 10))

for _ in range(10):
    # print(random.randrange(1, 10), end=" ")  # не включает 10
    print(random.randint(1, 10), end=" ")  # включает 10