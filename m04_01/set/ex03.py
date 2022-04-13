def is_unique(cheklist):
    return len(cheklist) == len(set(cheklist))

# проверка на уникальность


print(is_unique([1, 2, 3, 4]))
print(is_unique([1, 2, 3, 4, 5, 5]))
print(is_unique(["Red", "White", "Black", "Yellow"]))
print(is_unique(["Red", "White", "White", "Black", "Yellow"]))
