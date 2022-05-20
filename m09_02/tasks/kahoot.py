list_one = [5, 6, 7]
list_two = [2, 3, 4]


def func_one(lst):
    lst = lst * 2
    return lst


def func_two(lst):
    lst = lst.extend([1, 2, 3])  # None
    return lst


r_one = func_one(list_one)
r_two = func_two(list_two)

print(r_one, r_two)
print(list_one, list_two)