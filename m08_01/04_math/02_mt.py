import math

print(0.1 + 0.2 == 0.3)
r = math.isclose(0.1 + 0.2, 0.3)
print(r)

r = math.isclose(0.1, 0.10000000009)
print(r)

print(abs(0.1 - 0.1001) < 0.00001)
r = math.isclose(0.1, 0.1001, abs_tol=0.00001)
print(r)
