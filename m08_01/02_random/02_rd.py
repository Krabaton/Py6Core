import random

l = list(range(1, 37))
print(l)

random.shuffle(l)
print(l)

print(random.choice(l))
print(random.sample(l, k=5))
