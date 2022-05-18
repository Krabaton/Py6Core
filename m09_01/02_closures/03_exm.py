# Мемоизация с замыканием

def factorial_with_cache():
    cache = {}

    def calc(n):
        if n < 0:
            raise ValueError('Number not be negative')

        result = 1
        for val in range(1, n + 1):
            if val in cache:
                result = cache[val]
            else:
                result = val * cache.get(val - 1, 1)
                cache[val] = result
                print(f'{val} not in cache {result}')
        return result

    return calc


factorial = factorial_with_cache()

f3 = factorial(3)
print(f'f3: {f3}')

f5 = factorial(5)
print(f'f5: {f5}')

factorial(4)
