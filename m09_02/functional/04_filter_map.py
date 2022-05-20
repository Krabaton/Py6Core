# Map and filter

# 1
nums = [i for i in range(1, 10)]
print(nums)
sq = map(lambda x: x ** 2, nums)
result = filter(lambda value: bool(value % 2), sq)
print(list(result))

# 2
result = filter(lambda value: bool(value % 2), map(lambda x: x ** 2, [i for i in range(1, 10)]))
print(list(result))

# 3
result = map(lambda x: x ** 2, filter(lambda value: bool(value % 2), [i for i in range(1, 10)]))
print(list(result))
