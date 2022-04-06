def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 5! = 120
