# Sum i = 1 to infinity => (-1)^i/(i+1)!  epsilon = 0.0001

print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)
print(0.3)

print(abs(0.3 - (0.1 + 0.2)) <= 0.0001)


def factorial(n):
    if n < 2:
        return 1
    else:
        return factorial(n - 1) * n


def sum_inf(epsilon=0.000001):
    i = 1
    sum = (-1)**i / factorial(i + 1)
    while True:
        i += 1
        temp = (-1)**i / factorial(i + 1)
        if abs(temp) < epsilon:
            break
        sum = sum + temp
    return sum


print(sum_inf(0.0001))
print(sum_inf(0.000001))
